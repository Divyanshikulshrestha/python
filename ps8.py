# def maximum(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m=maximum(3,5,8)   
# print("the value of the maximum is "+ str(m))     



# def farh(cel):
#     return (cel*(9/5))+32
# c=45
# f=farh(c)
# print("fahreheit temperature is " + str(f))



# print("hello ",end="")
# print("how ",end="")
# print("are ",end="")
# print("you? ",end="")


# n!=(n-1)!*n
# sum(n)=sum(n-1)+n

# n=6
# for i in range(n):
#     print("*" * (n-i))

def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()



this="       harry is a good      "
n=remove_and_split(this,"harry")
print(n)
# print(this)
# print(this.strip)