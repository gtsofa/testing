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

    def __repr__(self):
        return "Employee('{}' '{}' '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    # turning a regular mtd to a classmethod
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
# Developer inherit from Employee
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        #Super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

# Manager inherit from Employee
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:

            self.employees.append(emp)

    

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:

            print('-->', emp.fullname())

dev_1 = Developer('tsofa', 'nyule', 6000, 'Python')
dev_2 = Developer('samule', 'mgogo', 7000, 'Java')

mgr_1 = Manager('Francis', 'Mramba', 9000, [dev_1])

print(dev_1.__str__())
print(dev_2)

print(dev_1 + dev_2)

#mgr_1.add_emp(dev_2)


#print(mgr_1.email)
#mgr_1.print_emps()

#print(isinstance(mgr_1, Manager))

#nice helper method
#print(help(Developer))

#print(dev_1.email)
#print(dev_1.prog_lang)

