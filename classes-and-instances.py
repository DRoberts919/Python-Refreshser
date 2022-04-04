# python obejct-oriented Programming. 


from cgi import print_arguments


class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@company'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



        

emp_1 = Employee('corey','schafer',5000)
emp_2 = Employee('test', 'User', 60000)

# print(emp_1)
# print(emp_2)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())