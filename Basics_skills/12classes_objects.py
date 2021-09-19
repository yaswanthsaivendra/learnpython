#objects are an encapsulation of variables and functions into single entity.
#objects get their variables and functions from classes.
#classes are essentially a template to create your objects.

class MyClass:
    var = "blah"

    def function(self): #To be specific, this is a method.
        print("This is a function inside the class MyClass")

myobjectx = MyClass()
myobjecty= MyClass()

myobjectx.var = "yeah"

print(myobjectx.var)
print(myobjecty.var)

myobjectx.function()

#A method in python is similar to function with these major differences :
    # unlike function, a method is called on an object.
    # method is accessible to data that is contained within the class.

#For now, its enough. we can learn complete details of methods and the use of self as default argument in the above method in further sections.