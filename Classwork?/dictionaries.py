#dictionaries have key:value for the elements
class_dict = {
    "class" : "Astr 19",
    "prof"  : "Brant",
    "stoke level" : 7.9
}
#will give out data type of "class_dict"
print(type(class_dict)) 

#get a value via key
course = class_dict["class"]
print(course)

#will change a value via key (increase stoke level)
class_dict["stoke level"] += 1
print(class_dict)

#print dictionary elemt by element
for x in class_dict.keys():
    print(x,class_dict[x])
