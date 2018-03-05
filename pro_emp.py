class Employee:
    """model employee class"""

    # class variable
    num_of_employees = 0
    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        """constructor ie initializer """
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        """return employee full name"""
        return self.first + ' ' + self.last

emp_1 = Employee('Julius', 'Nyule')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())