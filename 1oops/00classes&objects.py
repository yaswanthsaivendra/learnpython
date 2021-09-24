#classes are used to create user-defined data structures, they consists of data-variables and fucntions(called methods). 
#objects are instances of classes.
#classes are essentially a template to create your objects.

class DogClass :    #naming convention for class name - first letter of everyword should be captilazed.
    pass

class Dog:
    species = "bulldog" #class attribute
    def __init__(self, name, age):  #__init__ method is where we define all the instance attributes needed for the class.
        self.name = name            #Whenever an instance(i.e.,object) is created, this method will be executed first and intializes the object with these attributes.
        self.age = age
    #An instance attribute is unique for every instance(i.e., object) whereas we also have class attribures which are same for every object we created with this class.
    #usually class attributes are created at the start of the class.
    
    # We have three types of methods in python, one of them is Instance methods which we are using right now.
    #All instance methods have one default parameter - self, which points to the instance of the class.
    # Any method we create inside the class is an instance method unless we explicitly specify them as other type of methods.

#creating an instance of class is called - Instantiation.
obj=Dog("jimmy",10) #instance attributes defined inside the __init__ should be passed as arguments when creating the object.
#When an instance method is self argument is replaced with object.(__init__ method is automatically called when creating the object).


class Dog:
    species = "bulldog" 
    def __init__(self, name, age):  
        self.name = name            
        self.age = age
    
    #instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

obj=Dog("jimmy",12)
print(obj.speak("bow bow"))

#we can change what gets printed by defining a speical instance method called __str__().

class Dog:
    species = "bulldog" 
    def __init__(self, name, age):  
        self.name = name            
        self.age = age
    
    #instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

obj=Dog("jimmy",12)
print(obj)

#methods like .__init__ and .__str__ (start and end with double underscores) are called dunder methods.
