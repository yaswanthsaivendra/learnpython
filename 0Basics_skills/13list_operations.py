#Operations on list
## Methods
list1=["sai","raja","yash vendra"]
print(list1[0].upper())#upper method makes all letters to uppercase.upper and lower are most useful when taking input from users to avoid case sensitive probs.
name=input("enter any name: ").lower()
print(name)

print(list1[-1].title())#it capitilizes first letter of every word in the string.

#we can add an element to the list at the end by using append method.
list1.append("anu")
print(list1)

#we can add an element to the list at any place by using insert method.
list1.insert(1,"arjun")#remaining elements are self adjusted . standard way of using list.insert(index,"string_value")
print(list1)

#strip method-eleminating blank space
name="  yash  "
print(name.lstrip())#strip from left side
print(name.rstrip())#strip from right side
print(name.strip())#strip from both the sides.

#pop method-used to remove an element from a list by using it's index and store it for further use.
poped_element=list1.pop(1)
print(list1)
print(poped_element)

#remove method-removing an element from the list by using it's value.
list1.remove("sai")
print(list1)

#sort method-used to sort a list permanently.
list1=["sai","raja","yash vendra","anu"]
list1.sort()#to sort a list in alphabetical order
print(list1)

list1.sort(reverse=True)#to sort a list in reverse alphabetical order
print(list1)

#reverse method-it reverse the order of elements in list
print(list1.reverse())





##Functions
list1=["sai","raja","yash vendra","anu"]
#sorted function-used to sort a list temporarily.
print(sorted(list1))#sort a list alphabetically.
print(list1)
#len function used to find length.
print(len(list1))
#range function

for num in range(1,6):#excludes the end value(i.e.,num value changes from 1 to 5)
	print(num)

for even_num in range(2,11,2):#takes third argument as a difference
	print(even_num)

#list function is used along with range fun,to create a list.

even_num_list=list(range(2,11,2))
print(even_num_list)

#code to create a list of squares of num. from 1 to 10
squares=[]
for num in range(1,11):
		squares.append(num**2)
print(squares)


#min,max and sum functions:
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

#round function(roundoff func.)
print(round(3.9))
print(round(4.5))
print(round(3.5))




##del keyword in python.
#The primarly use of del keyword is to delete objects in python(ie.,variables,lists,dictionaries....everything).
#But mostly del keyword is used to delete an element in lists and dictionaries.
list1=["sai","raja","yash vendra"]
del list1[0]
print(list1)

dict1={
    "name":"yash",
    "age" : 18,
    "surname": "vendra",
}
del dict1["age"]
print(dict1)

