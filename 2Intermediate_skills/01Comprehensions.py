#List, dictionary and set comprehensions.

#List comprehensions
#list comprehensions are somewhat faster than normal for loops, however we dont use comprehensions in case of complex code, we make sure that our program is user friendly and readable.
#Every list comprehension can be rewritten in for loop, but we cannot rewrite every loop in list comprehension.

#usual way without list comprehensions to create 2 powers of numbers from 1 to 5.
numbers=[]
for i in range(1,6):
    numbers.append(2**i)
print(numbers)
#with list comprehensions.
numbers=[2**i for i in range(1,6)]

#we can add a optional coditional statement to comprehensions.
#program to get sqrt of numbers if they are even.
import math
numbers=[1,4,9,16,25,36]
new_list=[math.sqrt(n) for n in numbers if n%2==0]
print(new_list)

#we can have multiple for loops in list comprehensions.

team1=["john","alice","bob"]
team2=["shubham","dev","om"]

new_list= [(x,y) for x in team1 for y in team2] #this is same as like nested for loops in c, so we are going to have 3 X 3 = 9 tuples .
print(new_list)


#set comprehensions
word = "programming"
alphabets={x for x in word}
print(alphabets) #we get elements uniquely, since sets dont repeat elements.



#dict comprehensions
#program to map number and its square value as key-pairs of dict.

numbers=[1,2,3,4,5]
square_dict = dict()

for num in numbers:
    square_dict[num]=num**2
print(square_dict)

#same program using dict comprehensions
numbers=[1,2,3,4,5]
square_dict={i:i**2 for i in numbers} # dictionary = {key:value for vars in iterable}
print(square_dict)

#example2
original_dict = {"jack":12, "bob":18, "alice" :20, "rick" : 33}
even_dict = {k:v for (k,v) in original_dict.items() if v%2==0}
print(even_dict)

#we can also other conditionals like if-else.
#dict comprehensions can sometimes make code run slower .



