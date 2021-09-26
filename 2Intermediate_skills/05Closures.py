# Closures should be implemented when we met the following requirements:
#1. We must have a nested function (function inside a function).
#2. The nested function must refer to a value defined in the enclosing function.
#3. The enclosing function must return the nested function.

# Closures can avoid the use of global variables.
# Closures can be used rather than classes when we have a single method and fewer number of attributes. 
# But, if we have more numbers of methods and attributes, In such cases,S We should use classes only.

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

#multiplier of 4
times4 = make_multiplier_of(4)  #Here in this line, make_multiplier_of function execution is completed.
print(times4(10))       # But, in this line, we are still able to use the local variables of make_multiplier_of() function by calling times4 object as function(as we returned multiplier function, we will get an object as function).
#this is the beauty of decorators.

#multiplier of 7
times7 = make_multiplier_of(7)
print(times7(12))


#Note points:
#1. In python, we can define a function inside a function.
#2. In python, as everything is object, we can pass a fucntion as a argument to another function.