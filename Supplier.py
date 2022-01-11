from DTO_Object import DTO_Object


class Supplier (DTO_Object):

    def __init__(self, id, name):
        super().__init__(id, "Supplier")
        self.name = name
