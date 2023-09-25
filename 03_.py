# b="harry's" # use this if you have singel quotes in your strings
# b='harry"s' # use this if you have double quotes in your strings
# b='''harry"s''' # you can also use this in your strings
# # triple code is also use to write string in multiple line like this below
# b=''' divyanshi
# kulshrestha'''
# print(b)
# print(type(b))



# greating ="good night,"
# name = "divyanshi"
# print(type(name))
# # concatinating two strings
# c = greating + name
# print(c)


# name = "divyanshi"
# print(name[4])
# # name[3]="r" ----> it does not work


# # string sclicing
# print(name[0:5])
# print(name[:5]) # is same as print(name[0:5])
# print(name[3:]) # is same as print(name[3:8])
# # negative string
# print(name[-4:-1])


# #skiping in string
# d=name[0::3]
# print(d)



story = "once upon a time there was a student divyanshi who study programming from youtube"

# string function 
print(len(story))
print(story.endswith("youtube"))
print(story.count("a"))
print(story.capitalize())
print(story.find("divyanshi"))
print(story.replace("divyanshi","divya"))

#escape sequence character 
story="world is full of \\ fake smile \nits hard to \t except"
print(story)
