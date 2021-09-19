#slicing the list - using a part of the list.
names=["sai","raja","yash","vendra","anu","arjun"]#if we don't mention the first and last indices of a list, by default first =0 and last is taken up to the last element.
print(names[0:2])#prints first two elements in the list
print(names[0: :2])#third parameter is taken as difference

#In lists, we can use negative indices.
print(names[-1])#prints the last element in the list.

#using slice in a for loop
for name in names[:3]:
	print(name.upper())

#use slicing to copy lists.
names1=names[:]#if we dont use slicing then the two variables(names & names1) point to the same list,it doesnt mean of making a copy
print(names1)

#copy module (contains copy and decopy functions)
import copy
list1=["dog","cat","mouse"]
list2=copy.copy(list1)
list2[1]=20
print(list1)
print(list2)

#we can have lists in a list and we use the individual items in the list using multi indexing
pets=[["dog","cat","mouse"],["rabbit","horse","pigeon"]]
print(pets[1])
print(pets[0][1])



##slicing in strings
#A string is a character array.
firstname = "yaswanth"
for letter in firstname: #In each iteration of loop, a single letter from firstname is assigned to letter variable.
    print(letter)

#using some part of string - slicing
print(firstname[0])
print(firstname[1:3])

