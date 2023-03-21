#Why Classes?
#  Group Data & Functions- To Reuse & Easy to build upon
# attributes and Methods

"""
Employee

"""
class Employee:

    def __init__(self,first,last,pay) -> None:
        self.pay = pay
        self.first = first
        self.last = last
        self.email = first +'.'+last+'@company2.com'


emp1 = Employee('ketan','butte',60000)
emp2 = Employee('virat','kohli',800000)
# print(emp1)
# print(emp2)

print(emp1.email)
print(emp2.email)

