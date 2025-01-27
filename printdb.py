from persistence import *

def printActivities():
    table_list = repo.activitis.find_all("date")
    print("Activities")
    for act in table_list:
        print(act.__str__())

def printBranches():
    table_list = repo.branches.find_all("id")
    print("Branches")
    for branch in table_list:
        print(branch.__str__())

def printEmployees():
    table_list = repo.employees.find_all("id")
    print("Employees")
    for emp in table_list:
        print(emp.__str__())

def printProducts():
    table_list = repo.products.find_all("id")
    print("Products")
    for prd in table_list:
        print(prd.__str__())

def printSuppliers():
    table_list = repo.suppliers.find_all("id")
    print("Suppliers")
    for sup in table_list:
        print(sup.__str__())

def employeesReport():
    c = repo._conn.cursor()
    c.execute("""SELECT employees.name, employees.salary, branches.location
                FROM employees INNER JOIN branches ON employees.branche = branches.id
              ORDER BY employees.name
             """)
    rows = c.fetchall()
    for row in rows:
        print("%s, %s, %s" % ((row[0].decode('utf-8')),row[1],row[2].decode('utf-8')))





def main():
    printActivities()
    printBranches()
    printEmployees()
    printProducts()
    printSuppliers()

if __name__ == '__main__':
    employeesReport()
    