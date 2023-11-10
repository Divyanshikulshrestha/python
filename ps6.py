# num1=int(input("enter no.1 :"))
# num2=int(input("enter no.2 :"))
# num3=int(input("enter no.3 :"))
# num4=int(input("enter no.4 :"))
# if(num1>num4):
#     f1=num1
# else:
#     f1=num4
# if(num2>num3):
#     f2=num2
# else:
#     f2=num3
# if(f1>f2):
#     print(str(f1)+"  is greatest")
# else:
#     print(str(f2)+"  is greatest")    


# sub1=int(input("enter sub1 marks\n"))
# sub2=int(input("enter sub2 marks\n"))
# sub3=int(input("enter sub3 marks\n"))
# per=(sub1+sub2+sub3)/3
# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail")
# if(per<40):
#     print("you are fail due to total percentage less than 40")
# else:
#     print("you are pass")
# print(per)



# text=input("enter the text \n")
# if("make a lot of money" in text):
#     spam=True
# elif("buy now" in text):
#     spam=True
# elif("click this" in text):
#     spam=True
# elif("subscribe this" in text):
#     spam=True
# else:
#     spam=False
# if(spam):
#     print("this text is spam")
# else:
#     print("this text is not spam")



# names=["harry","shubham","rohit","aditi","shipra"]
# name=input("enter the name to check\n")
# if name in names :
#     print("your name is present in the list")
# else:
#     print("your name is not present in the list")



marks=int(input("enter your marks"))
if marks>=90:
    grade="Ex"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=50:
    grade="D"
else:
    grade="F"
print("YOUR GRADE IS " + grade)