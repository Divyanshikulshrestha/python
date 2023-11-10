# class Number:
#     def sum(self):
#         return self.a+self.b
# num=Number()
# num.a=12
# num.b=34
# s=num.sum()
# print(s)
# '''
# PasscalCase
# EmployeeName-->PascalCase

# CamelCase
# isNumeric, isFlot -->camelCase
# '''
# import pandas as pd
# pd.DataFrame()
# class RailwayForm:
#     formType="RailwayForm()"
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Train is {self.train}")
# harrysApplication=RailwayForm()
# harrysApplication.name="Harry"
# harrysApplication.train="Rajdhani Express"
# harrysApplication.printData()

# class Remote:
#     pass
# class Player:
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
#     def moveTop(self):
#         pass
# remote1 = Remote()
# player1 = Player()

# if(remote1.isLeftpressed()):
#     player1.moveLeft()

# class Employee:
#     company = "Google"
#     salary=100
# harry = Employee()
# rajni = Employee()

# # creating instance attribute salary for both the objects
# # harry.salary=300
# # rajni.salary=400
# harry.salary=45
# print(harry.salary)
# print(rajni.salary)
# print(rajni.address) ---> throughs an error
# print(harry.company)
# print(rajni.company)
# Employee.company="YouTube"
# print(harry.company)
# print(rajni.company)



# class Employee:
#     company = "Google"
#     def getSalary(self):
#         print(f"Salary for this employee working in {self.company} is {self.salary}")

# harry = Employee()
# harry.salary = 100000
# harry.getSalary()     # Employee.getSalary(harry)





# class Employee:
#     company = "Google"
#     def getSalary(self,signature):
#         print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")
#     @staticmethod
#     def greet():
#         print("good mornig, sir")
#     @staticmethod
#     def time():
#         print("the time is 9AM in the morning")
# harry = Employee()
# harry.salary = 100000
# harry.getSalary("thanks!")     # Employee.getSalary(harry)
# harry.greet()            # Employee.greet()
# harry.time()



class Employee:
    company = "Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created!")

        def getDetails(self):
            print(f"the name of the employee is {self.name}")
            print(f"the salary of the employee is {self.salary}")
            print(f"the subunit of the employee is {self.subunit}")

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} \n {signature}")
    @staticmethod
    def greet():
        print("good mornig, sir")
    @staticmethod
    def time():
        print("the time is 9AM in the morning")

harry=Employee("harry",100,"youtube")
# harry=Employee()   ---> this through an error (missing three required positional arguments:)
harry.getDetails()