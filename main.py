import sys

#from Repository import repo
from Hat import Hat
from Supplier import Supplier


def print_hi(name):

    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

    #config = sys.argv[0]
    #orders = sys.argv[1]
    #output = sys.argv[2]
    #database = sys.argv[3]

    #repo.create_tables(database)

    config_text = open("config.txt", "r+").read()
    print(config_text)
    #firstLine = config_text.readline()
    numOfHats = config_text[0: config_text.find(',')]
    numOfSupp = config_text[config_text.find(',')+1 : config_text.find('\n')]
    print(numOfSupp)

    counter = 0
    for line in config_text.split('\n'):
        split = line.split(',')
        if 0 < counter <= numOfHats:
            Hat(split[0], split[1], split[2], split[3])
        elif counter > numOfHats:






