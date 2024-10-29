x = [0.0, 3.0, 5.0, 2.5, 3.7] #defines a list
print(type(x))   #prints out data type

#will remove the third element
x.pop(2)
print("x.pop(2)? okay,", x)

#will remove the elelmt equal to 2.5
x.remove(2.5)
print("x.remove(2.5)? okay,", x)

#will add an element at the end
x.append(1.2)
print("x.append(1.2)? okay,", x)

#get a copy of the list
y = x.copy()
print("y = x.copy()? okay,", y)

#how many elements are 0.0
print("y.count(0.0)? okay,",y.count(0.0))

#print the index with value 3.7
print("y.index(3.7)? okay,", y.index(3.7))
#begins to count from 0 making 3.7's index, 2

#sort the list
y.sort()
print("y.sort()", y)

#reverse the list
y.reverse()
print("y.reverse()?", y)

#remove all elements
y.clear()
print("y.clear()?", y)