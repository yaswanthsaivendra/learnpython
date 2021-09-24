#tuples - these are the lists that cannot be changed(immutable).
dimensions = (30,40)#we use parenthesis instead of square brackets
print(dimensions)
#we can't change a value in tuples but we can rewrite the tuples..
dimensions = (40,50)
for dimension in dimensions:
    print(dimension)

t=(1,2,3,4,5,6,7,8,9)
#Other than immutability, everything is almost same. we can access elements using index.
print(t[0])
print(t[1::2])
#tuple is somewhat faster than list, should be used when we dont want to change the elements.
t=(2,) #singleton tuple should be declared using a comma at the end, otherwise it treated as based as int or string or other thing based on the data.


#packing and unpacking in tuples
t=(1,2,3,4) #packing
#unpacking
(e1,e2,e3,e4)=t #while unpacking, elements at the left should match the no. of elements in the tuple.
print(e1)
print(e2)
#unpacking and packing can be combined into one statement.
(e1,e2,e3,e4)=(1,2,3,4)#no. of elements at the left and right should be same.


#In tuples, parenthesis can be ignored.
t=1,2,3,4 #tuple packing
print(t)
print(type(t))
t=1, #singleton tuple
e1,e2,e3,e4 = 1,2,3,4 #It looks like normal assignment, but it acts like a tuple.

#swap using tuple
a=1
b=2
a,b=b,a #swapped the elements without any need of third variable.
print(a)
print(b)





