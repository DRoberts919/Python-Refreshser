# python obejct-oriented Programming. 




from email.policy import EmailPolicy
from types import ClassMethodDescriptorType


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@company'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def fromString(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)




        

emp_1 = Employee('corey','schafer',5000)
emp_2 = Employee('test', 'User', 60000)

# print(emp_1)
# print(emp_2)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



# class method to update string
emp_str_1 = 'johh-Doe-7000'
emp_str_2 = 'Steve-smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.fromString(emp_str_1)
print(new_emp_1.email)