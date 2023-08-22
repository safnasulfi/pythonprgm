employee = {"id":100,"name":"vijay","department":"hr","salary":250000}

def get_name(emp):
    return emp.get("name")
print(get_name(employee))

emp_name = lambda emp:emp.get("name")
print(emp_name(employee))

emp_salary = lambda emp:emp.get("salary")
print(emp_salary(employee))

