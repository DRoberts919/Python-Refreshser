# python obejct-oriented Programming. 



class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@company'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,language):
        super().__init__(first,last,pay)
        self.language = language
        

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)

dev_1 = Developer('corey','schafer',5000,"python")
dev_2 = Developer('test', 'User', 60000,'java')


print(dev_1.email)
print(dev_1.language)
print(dev_2.email)
print(dev_2.language)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

