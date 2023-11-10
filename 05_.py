# mydict={
#     "fast":"in a quick manner",
#     "harry":"a coder",
#     "marks":[1,2,5],
#     "anotherdict":{'harry':'player'}
# }
# # print(mydict['fast'])
# # print(mydict['harry'])
# mydict['marks']=[45,78]
# print(mydict['marks'])
# print(mydict['anotherdict']['harry'])


# methods in dectionary
# mydict={
#     "fast":"in a quick manner",
#     "harry":"a coder",
#     "marks":[1,2,5],
#     "anotherdict":{'harry':'player'},
#     1:2
# }
# #dictionary methods
# print(list(mydict.keys()))      #print the keys of the dictionary
# print(list(mydict.values()))    #prints the keys of the dictionary
# print(list(mydict.items()))     #print the (key,value) for all contents of the dictionary
# print(mydict)
# updatedict={
#     "lovish":"friend",
#     "divya":"friend",
#     "shubhum":"friend",
#     "harry":"a dancer"
# }
# mydict.update(updatedict)       #update the dictionary by adding key-value pairs from updatedict 
# print(mydict)
# print(mydict.get("harry"))     #print value associated with key "harry"
# print(mydict["harry"])         #print value associated with key "harry"
# #the difference between .get and [] syntax in dictionary
# print(mydict.get("harry2"))     #return none as harry2 is not present in the dictionary
# print(mydict["harry2"])         #through an error as harry2 is not present int the dictionary

# sets in python
a={1,2,3,4,5,1}
print(type(a))
print(a)

# important:this syntax will created an empty dictionary and not set
a={}
print(type(a))

# an empty set can be created using the below syntax
# creating an empty set
b=set()
print(type(b))
# adding values to an empty set
b.add(4)
b.add(5)
b.add(4) #same element is not print in set
b.add(5)
b.add(4)
b.add(5,4,6)  #can't add list in a set 
#accessing element
b.add({4:5})  #can't add dictionary in a set 
b.add((5,6,4)) #but can add tuple in a set
print(b)

# length of the set
print(len(b)) #print the length of the set
# removal of an item
b.remove(5) #remove 5 from set b
# b.remove(15) #through an error while trying to remove 15 (which is not in the set)
print(b)

print(b.pop())
print(b)