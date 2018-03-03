# Class Employee playing ground.

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

    def apply_raise(self):
        """return total pay after salary raise"""
        #return int(self.pay * 1.05)
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_employees)

emp_1 = Employee('tsofa', 'nyule', 6000)
emp_2 = Employee('samule', 'mgogo', 7000)

print(Employee.num_of_employees)
