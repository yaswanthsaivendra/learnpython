#lists
mylist = []     #creating an empty list
mylist2= [1,2,3,4,5] #creating a list with elements.
mylist.append(1)    #we can append an element using append method.
mylist.append(2)

#we can access elements using index
print(mylist[0])
#accessing an index which doesn't have an element throws an error.
#print(mylist[5])   throws an error.

#we can do list concatenation and list replication too..
list_one =["sai","yash","vendra"]
list_two =["raja","anu","giri"]
print(list_one+list_two)      #list concatenation
print(list_one * 3)           #list replication