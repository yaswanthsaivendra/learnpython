class Dog:              #parent class
    species = "bulldog" 
    def __init__(self, name, age):  
        self.name = name            
        self.age = age
    
    #instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

#child classes
#child classes inherit the methods and attributes from parent class.
#child classes can override or extend the attributes and methods of parent class.
class DogName1(Dog):    #child classes are created by passing parent class as argument.
    pass

class DogName2(Dog):
    pass

jimmy=DogName1("jimmy",6)
jack=DogName2("jack",8)

print(jack)
print(jimmy.speak("woof"))

#we can check an instance belongs to which class using isinstance().
print(isinstance(jimmy,Dog))    #isinstance(obj,class)
#instances of child classes are considered as instances of parent class also.
 

class DogName3(Dog):
    def speak(self, sound="Arf"):   #we just overrided the speak method of parent class by defining the method with the same name.
        return f"{self.name} barks {sound}"

julie=DogName3("julie",8)
print(julie.speak())

#we can access parent class methods in the methods of child classes using super()
class DogName3(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

julie=DogName3("julie",8)
print(julie.speak())