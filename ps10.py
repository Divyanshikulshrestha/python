# class Programmer:
#     company="Microsoft"
#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
#     def getInfo(self):
#         print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
# harry = Programmer("harry","skype")
# alka = Programmer("alka","github")
# harry.getInfo()
# alka.getInfo()



# class Calculator:
#     def __init__(self,num):
#         self.number=num
    
#     def square(self):
#         print(f"the value of {self.number} square is {self.number**2}")
    
#     def squareroot(self):
#         print(f"the value of {self.number} squareroot is {self.number**0.5}")

#     def cube(self):
#         print(f"the value of {self.number} cube is {self.number**3}")

# a=Calculator(9)
# a.square()
# a.squareroot()
# a.cube()



# class Sample:
#     a="harry"
# obj =Sample()
# obj.a="vikky"  #it set new instent attribute
# # Sample.a="vikky"   it change class attribute
# print(Sample.a)
# print(obj.a)




# class Calculator:
#     def __init__(self,num):
#         self.number=num
    
#     def square(self):
#         print(f"the value of {self.number} square is {self.number**2}")
    
#     def squareroot(self):
#         print(f"the value of {self.number} squareroot is {self.number**0.5}")

#     def cube(self):
#         print(f"the value of {self.number} cube is {self.number**3}")
   
#     @staticmethod
#     def greet():
#         print("*****hello there welcome to the best calculater of the word*****")

# a=Calculator(9)
# a.greet()
# a.square()
# a.squareroot()
# a.cube()



# class Train:
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
    
#     def getStatus(self):
#         print("***********")
#         print(f"the name of the train is {self.name}")
#         print(f"the seats available in the train are {self.seats}")
#         print("***********")
#     def fareInfo(self):
#         print(f"the price of the ticket is: rs.{self.fare}")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"your ticket has been booked! your seat no. is {self.seats}")
#             self.seats=self.seats-1
#         else:
#             print("sorry this train is fulled kindly try in tatkal")

# intercity = Train("intercity express:14015",90,2)        
# intercity.getStatus()
# # intercity.fareInfo()
# intercity.bookTicket()
# intercity.getStatus()



class Sample:
    def __init__(slf,name):
        slf.name=name
obj =Sample("harry")
print(obj.name)