# To create custom iterators, we have to do lot of work. Generators comes to the rescue.
# generators - are a simply way of creating iterators.
#generator is a fucntion which returns an object (i.e., iterator).

def even_generator(max):
    n=2
    while n<=max:
        yield n #an yield statement, pauses the function and stores it current state . later it passes the state of the fucntion in futher function calls.
        n+=2
num=even_generator(6)   #iterator object
print(next(num))
print(next(num))
print(next(num))

#generator expressions