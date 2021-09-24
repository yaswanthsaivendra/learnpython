# set 
lang = {"c", "python", "java", "python"}
print(lang)  # set does not consider duplicates,So it return elements uniquely.

# A set can have any numbers of times and they may be of different types.(int,float,tuple,string etc..)
# But, a set cannot have mutable elements like lists,sets and dictonaries as its elements.
my_set= {1, "hello", (1,2,3)}
print(my_set)

# set does not support indexing or slicing.

##Adding elements to a set
# We can add a single element using add() method, and multiple elements using update() method. update() method can take tuples, lists, strings or other sets as arguments.
my_set={1,5,3}
my_set.add(2)
print(my_set)

my_set={1,5,3}
my_set.update({1,2},["a","b"],(34,66))
print(my_set)


##Deleting elements from a set.
# We have two methods for this purpose, remove() and discard().
# The only difference b/w these two methods is, disard() method ignores when it doesnt find the element it has to delete whereas remove() method raises an error.
my_set={1,2,3,4}
my_set.discard(1)
print(my_set)
my_set.remove(2)
print(my_set)

my_set.clear()      #clear all elements in the set.



#Sets - are just like sets in math, we can perform mathematical set operations on sets.

#union (A U B)
A={1,2,3,4,5,6}
B={5,6,7,8,9,10}

print(A.union(B))   #union method
print(B.union(A))   #union method
print(A | B)        #union operation can also be achieved using | operator.


#Intersection

print(A.intersection(B))   #intersection method
print(A & B)        #intersection operation can also be achieved using & operator.

#Set difference (A-B)

print(A.difference(B))   #difference method
print(A - B)        #set difference operation can also be achieved using - operator.

#Set symmetric difference ((A U B) - (A intersection B))
# Elements which are there in either of the sets, but not in both of them.
print(A.symmetric_difference(B))   #symmetric_difference method
print(A ^ B)        #set symmetric difference operation can also be achieved using ^ operator.


# Python Frozenset
# Frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictonary keys.
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.
#these will be created by using frozenset() function.

A = frozenset([1,2,3,4])
print(A)
