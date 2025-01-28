from persistence import *

def printActivities():
    table_list = repo.activitis.find_all_by_order("date")
    print("\nActivities\n")
    for act in table_list:
        print(act.__str__())

def printBranches():
    table_list = repo.branches.find_all_by_order("id")
    print("\nBranches\n")
    for branch in table_list:
        print(branch.__str__())

def printEmployees():
    table_list = repo.employees.find_all_by_order("id")
    print("\nEmployees\n")
    for emp in table_list:
        print(emp.__str__())

def printProducts():
    table_list = repo.products.find_all_by_order("id")
    print("\nProducts\n")
    for prd in table_list:
        print(prd.__str__())

def printSuppliers():
    table_list = repo.suppliers.find_all_by_order("id")
    print("\nSuppliers\n")
    for sup in table_list:
        print(sup.__str__())

def employeesReport():
    c = repo._conn.cursor()
    c.execute("""SELECT employees.name, employees.salary, branches.location, employees.id
                FROM employees INNER JOIN branches ON employees.branche = branches.id
              ORDER BY employees.name
             """)
    rows = c.fetchall()
    print("\nEmployees report\n")
    for row in rows:
        print("%s %s %s %s" % ((row[0].decode('utf-8')),row[1],row[2].decode('utf-8'),employeeIncom(row[3])))

def employeeIncom(employeeId : str) -> int:
    # calaculate for employee its total Transaction incom
    totalEmployeeIncom = 0
    employeeTransactionTable = repo.activitis.find(activator_id = employeeId)
    for transaction in employeeTransactionTable:
        productPrice = repo.products.find(id = transaction.product_id)[0].price  
        totalEmployeeIncom += productPrice * abs(transaction.quantity)
    return totalEmployeeIncom


def activitiesReport():
    print("\nActivities Report\n")
    c = repo._conn.cursor()
    c.execute("""
    SELECT activities.date, products.description, activities.quantity,
    CASE 
        WHEN employees.id IS NOT NULL THEN employees.name
        ELSE NULL
    END AS employee_name,         
    CASE
        WHEN suppliers.id IS NOT NULL THEN suppliers.name
        ELSE NULL
    END AS supplirs_name
    FROM activities
    INNER JOIN products ON products.id = activities.product_id
    LEFT JOIN employees ON employees.id = activities.activator_id
    LEFT JOIN suppliers ON suppliers.id = activities.activator_id
    """)
    rows = c.fetchall()
    for row in rows:
        if row[3] is None:
            print("('%s', '%s', %s, %s, '%s')" % ((row[0].decode('utf-8')),row[1].decode('utf-8'),row[2],"None",row[4].decode('utf-8')))
        else:
            print("('%s', '%s', %s, '%s', %s)" % ((row[0].decode('utf-8')),row[1].decode('utf-8'),row[2],row[3].decode('utf-8'),"None"))

    str = "fdas"
            
    




def main():
    printActivities()
    printBranches()
    printEmployees()
    printProducts()
    printSuppliers()
    employeesReport()
    activitiesReport()

if __name__ == '__main__':
    main()

    