# def percentage(marks):
#     p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
#     return p
# marks1=[45,56,67,78]
# percentage1=percentage(marks1)
# marks2=[34,45,56,67]
# percentage2=percentage(marks2)
# # percentage2=((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100
# print(percentage1,percentage2)



# def greet(name):
#     print("good day,"+ name)

# def sum(num1,num2):
#     return num1+num2
    
# greet("divyanshi")
# s=sum(6,36)
# print(s)



# def greet(name="stranger"):
#     print("good day,"+ name)
# greet("divyanshi")
# greet()

# n=0
# product=1
# for i in range(n):
#     product=product*(i+1)
# print(product)

def factorial_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
def factorial_recursive(n):
    if n==1 or n==1 :
        return 1
    return n*factorial_recursive(n-1)
# f=factorial_iter(5)
f=factorial_recursive(5)
print(f)


