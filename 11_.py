# single inheritance


# class Empoloyee:
#     company="Google"

#     def showdetails(self):
#         print("this is an employee")

# class Programer(Empoloyee):
#     language="Python"
#     company="youtube"

#     def getLanguage(self):
#         print(f"the language is {self.language}")

#     def showdetails(self):
#         print("this is an programmer")


# e=Empoloyee()
# e.showdetails()
# p=Programer()
# p.showdetails()
# print(p.company)


# multiple inheritance
# class Employee:
#     company="Visa"
#     eCode=120
# class Freelancer:
#     company="Fiverr"
#     level=0

#     def upgradelevel(self):
#         self.level=self.level+1

# class Programmer(Employee,Freelancer):
#     name="rohit"

# p=Programmer()
# p.upgradelevel()
# print(p.company)




# multilevel inheritance
# class Person:
#     country="India"

#     def takeBreath(self):
#         print("i am breathin...")

# class Employee(Person):
#     company="Honda"

#     def takeBreath(self):
#         print(f"i am an employee so i am luckily breathing...")

# class Programmer(Employee):
#     company="Fiverr"

#     def getSalary(self):
#         print(f"no salary to programmer")

#     def takeBreath(self):
#         print(f"i am an programmer so i am luckily breathing++ ")


# p=Person()
# p.takeBreath()
# # print(p.company)  #   ---->  it throughs an error

# e=Employee()
# e.takeBreath()
# print(e.company)

# pr=Programmer()
# pr.takeBreath()
# print(pr.country)



# super in python


# class Person:
#     country="India"

#     def __init__(self):
#         print("initializing person...\n")

#     def takeBreath(self):
#         print("i am breathin...")

# class Employee(Person):
#     company="Honda"

#     def __init__(self):
#         super().__init__()
#         print("initializing employee...\n")

#     def takeBreath(self):
#         super().takeBreath()
#         print(f"i am an employee so i am luckily breathing...")

# class Programmer(Employee):
#     company="Fiverr"

#     def __init__(self):
#         super().__init__()
#         print("initializing programmer...\n")

#     def getSalary(self):
#         print(f"no salary to programmer")

#     def takeBreath(self):
#         super().takeBreath()
#         print(f"i am an programmer so i am luckily breathing++ ")


# # p=Person()
# # p.takeBreath()

# #e=Employee()
# # e.takeBreath()

# pr=Programmer()
# # pr.takeBreath()




# class method in python



# class Employee:
#     company = "Camel"
#     salary = 100
#     location = "Delhi"

#     # def changeSalary(self,sal):
#     #     self.__class__.salary = sal

#     @classmethod
#     def changeSalary(cls,sal):
#         cls.salary = sal

# e = Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employee.salary)



# property decorater
# class Employee:
#     company="Bhrat gas"
#     salary=5600
#     salarybonus=400
#     # totalsalary=6100

#     @property
#     def totalsalary(self):
#         return self.salary + self.salarybonus
    
#     @totalsalary.setter
#     def totalsalary(self,val):
#         self.salarybonus=val-self.salary
    
# e=Employee()
# print(e.totalsalary)
# e.totalsalary=5800
# print(e.salary)
# print(e.salarybonus)


# operator overloading



# class Number:
#     def __init__(self,num):
#         self.num=num

#     def __add__(self,num2):
#         print("lets add")
#         return self.num + num2.num
    
#     def __mul__(self,num2):
#         print("lets multiply")
#         return self.num * num2.num
    
# n1=Number(4)
# n2=Number(6)
# sum=n1+n2
# mul=n1*n2
# print(sum)
# print(mul)


# other dunder method in python



class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num
    
    def __mul__(self,num2):
        print("lets multiply")
        return self.num * num2
    
    def __str__(self):
        return f"decimal number : {self.num}"
    def __len__(self):
        return 1
        
n=Number(9)
print(n)
print(len(n))
        
    
    