#Namespaces in python.
#Before understanding namespaces, first we have to understand what is name in python.

#we know in python, everything is an object.
a=2 #Here, 2 is an object and a is the name(also called identifier) given to the object.

print("id(2)=", id(2))
print("id(a)=", id(a))
#here we can see both have the same address, where 2 is an object and 'a' is the identifier of the object.

#To understand this better, look at the following example:
a=2
print("id(a)=", id(a))

a=a+1
print("id(a)=", id(a))
print("id(3)=", id(3))

b=2
print("id(b)=", id(b))
print("id(2)=", id(2))

#From the above three cases, we can clearly understand few things:
#From 1 & 2
# we can see that the address of a is changed from first case to second case.
# And in the second case, the address of 3 and 'a' was same.
# Here what happend is, firstly the object 2 was created and 'a' was used as name(idnetifer) for it. Later when we incremented the value of 'a', a new object was created which is 3 and now 'a' acts as identifier of 3 but not 2.

#From 2 & 3
#It is obvious that the address of b and 2 were same in third case.
#But if we clearly observe this, address in the third case , is actually address of the object 2 created in the first case.
#Here what happend is, in the current namespace we already have an object 2 without a name. So, in third case python interpreter rather than creating a new object, it used the existing object 2 and added b as a name(identifier) to it.


#Now comes to the point, what is a Namespace??
#Simply, namespace is a collection of names. namespace is a collection of names which are mapped to their coressponding objects.
#A Namespace exists, as long as the program runs.
#Different namespaces can co-exist at a given time but they are completely isolated.(It does mean that "a program (or) a part of the program with different namespaces can run at same time, but they wont get interrupted with each other.")

#A module(a python program file with .py extension) have a global namespace.
# Functions and classes have their local namespaces.


