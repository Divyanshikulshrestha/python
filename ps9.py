# f=open('poems.txt')
# t=f.read()
# if 'twinkle' in t :
#     print("twinkle is present")
# else:
#     print("twinkle is not present")
# f.close()







# def game():
#     return 68

# score = game()
# with open("highscore.txt") as f:
#     highscorestr = f.read()

# if highscorestr=="":
#     with open("highscore.txt","w") as f:
#         f.write(str(score))

# elif int(highscorestr)<score:
#     with open("highscore.txt","w") as f:
#         f.write(str(score))








# for i in range(2,21):
#     with open(f"table/multiprlicalion_table_of_{i}.txt","w") as f:
#         for j in range(1,11):
#             f.write(f"{i}*{j}={i*j}")
#             if j!=10:
#                 f.write('\n')
    






# with open("sample.txt") as f:
#     content=f.read()
# content=content.replace("donkey","$%^@$^#")
# with open("sample.txt","w") as f:
#     f.write(content)






# words=["donkey","kadu","mote"]
# with open("sample.txt") as f:
#     content=f.read()
# for word in words:
#     content=content.replace(word,"$%^@$^#")
# with open("sample.txt","w") as f:
#     f.write(content)







# content=True
# i=1
# with open("log.txt") as f:
#     while content:
#         content = f.readline()
#         if 'python' in content.lower():
#             print(content)
#             print(f"yes python is present on line number {i} ")
#         i+=1
        







# with open("this.txt") as f:
#     content=f.read()
# with open("copy.txt", "w") as f:
#     f.write(content)







# file1="copy.txt"
# file2="this.txt"
# with open(file1) as f:
#     f1=f.read()
# with open(file2) as f:
#     f2=f.read()
# if f1==f2:
#     print("files are identical")
# else:
#     print("files are not identical")







# filename="sample.txt"
# with open(filename,"w") as f:
#     f.write("")






import os
oldname ="sample2.txt"
newname="renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()
with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)