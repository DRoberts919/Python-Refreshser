# python obejct-oriented Programming. 




from email.policy import EmailPolicy


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



        

emp_1 = Employee('corey','schafer',5000)
emp_2 = Employee('test', 'User', 60000)

# print(emp_1)
# print(emp_2)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)