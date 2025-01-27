from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    branche = Branche(splittedline[0],splittedline[1],splittedline[2])
    repo.branches.insert(branche)

def add_supplier(splittedline : list[str]):
    supplier = Supplier(splittedline[0],splittedline[1],splittedline[2])
    repo.suppliers.insert(supplier)

def add_product(splittedline : list[str]):
    prod = Product(splittedline[0],splittedline[1],splittedline[2],splittedline[3])
    repo.products.insert(prod)

def add_employee(splittedline : list[str]):
    emp = Employee(splittedline[0],splittedline[1],splittedline[2],splittedline[3])
    repo.employees.insert(emp)

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    # inputfilename = args[1]
    inputfilename = "config.txt"
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)