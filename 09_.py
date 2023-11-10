# # use open function to read the content of a file!
# # f=open('sample.txt','r')
# f=open('sample.txt')   # by default the mode is r
# data=f.read(5)         # read first five character from the file
# print(data)
# f.close()



# f=open('sample.txt')
# # read 1st line
# data=f.readline       
# print(data)
# # read 2nd line
# data=f.readline       
# print(data)
# # read 3rd line
# data=f.readline       
# print(data)
# # read 4th line ... and so on...
# data=f.readline       
# print(data)
# f.close()



# f=open('another.txt','w')
# f.write("I am writting")
# f.close()


with open('another.txt','r') as f:
    a=f.read()
with open('another.txt','w') as f:
    a=f.write("me")
    print(a)