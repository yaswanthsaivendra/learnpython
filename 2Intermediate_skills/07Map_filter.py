#map and filter helps to shorter the code without the use of loops and branching.
#map and filter are built-in functions, comes within __builtins__ module.

#map function
#For example, we have to create a list of the square numbers of a list.
#the usual way of doing it with loops:
numbers=[1,2,3,4,5]
square_nums=[]
square= lambda n:n**2 
for i in numbers:
    square_nums.append(square(i))
print(square_nums)

#Doing the same with the use of map() fucntion.
numbers=[1,2,3,4,5]         #map(func,*iterables)
square_nums=list(map(lambda n:n**2,numbers))  #map() function returns a map object, so we have to list() constructor to convert it into list.
print(square_nums)

#map(func,*iterables)
#map function takes in a function as first argument and then n number of iterables as arguments.
#function - a function that perform some action to each element of an iterable
#iterable - an iterable like sets, lists, tuples, etc

#The map() function returns an object of map class. The returned value can be passed to functions like
#list() - to convert to list
#set() - to convert to a set, and so on.

#An example to work with mutiple parameters in lambda function with multiple iterables in map.
num1=[1,2,3]
num2=[4,5,6]
sumlist=list(map(lambda n1,n2:n1+n2,num1,num2))#here n1 takes numbers from num1 list and n2 from num2 list.
print(sumlist)


# filter() function
# The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.

numbers = [1, 2, 3, 4, 5, 6, 7]
# the lambda function returns True for even numbers 
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers) #filter(function, iterable)
#filter function returns an iterable.
# converting to list
even_numbers = list(even_numbers_iterator)
print(even_numbers)