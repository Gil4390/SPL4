import inspect

from Hat import Hat
from Supplier import Supplier


def row_map(row, col_mapping, dto_type):  # transfer row of the query to the corresponding DTO
    ctor_args = [row[idx] for idx in col_mapping]  # arrange the list in correct order
    return dto_type(*ctor_args)


def orm(cursor, dto_type):  # return array of DTOs that fit the last SQL query result records
    # retrieve constructor arguments’ names
    args = inspect.getargspec(dto_type.__init__).args  # todo check
    # args[0]=self, so we ignore it
    args = args[1:]
    # get names of data columns in cursor
    col_names = [column[0] for column in cursor.description]
    # map the names into the position of the corresponding constructor argument
    col_mapping = [col_names.index(arg) for arg in args]
    # transfer each row in cursor to DTO, and return list of DTOs
    return [row_map(row, col_mapping, dto_type) for row in cursor.fetchall()][0]


class DAO_Object:

    def __init__(self, dto_type, con):
        self._con = con
        self.dto_type = dto_type
        self.table_name = dto_type.__name__.lower() + 's'

    def insert(self, dto_instance):
        ins_dict = vars(dto_instance)
        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))

        stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self.table_name, column_names, qmarks)
        self._con.execute(stmt, list(params))

    def find_by_topping(self, val):
        c = self._con.cursor()
        c.execute("""
                    SELECT * FROM hats WHERE topping = ?
                """, [val])
        return Hat(*c.fetchone())

    def find_supplier(self, id):
        c = self._con.cursor()
        c.execute("""
                    SELECT * FROM suppliers WHERE id = ?
                """, [id])
        return Supplier(*c.fetchone())

    def update(self, id, new_val):
        self._con.execute('UPDATE {} SET quantity={} WHERE (id = {})'.format(self.table_name, new_val, id))

    def remove(self, id):
        stmt = 'DELETE FROM {} WHERE (id={})'.format(self.table_name, id)
        self._con.execute(stmt)
