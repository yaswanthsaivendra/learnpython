#defining a function 
def acc_user(username):
	"""display a greeting""" #docstring(enclosed in triple quotes)
	print(f"hello {username.title()}")

acc_user("yash")		#calling a function


#positional arguments
def pet_details(animal_type,name):
	"""display information about a pet"""	#docstring is a function short description.
	print(f"\n i have a {animal_type}")
	print(f" my {animal_type}'s name is {name}")

pet_details("dog","jimmie")

#keyword arguments(name-value pair arguments)
def pet_details(animal_type,name):
	"""display information about a pet"""
	print(f"\n i have a {animal_type}")
	print(f" my {animal_type}'s name is {name}")

pet_details(animal_type="dog",name="jimmie")

#Defaults(if we use default arguments for parameters while defining a function then they can be used as it is when no arguments are provided in function call)
def pet_details(name,animal_type="dog"):
	"""display information about a pet"""
	print(f"\n i have a {animal_type}")
	print(f" my {animal_type}'s name is {name}")

pet_details(name="jimmie")
#we must put non-default parameters first in function defintion in order to avoid errors and it is also helps to use positional arguments.
pet_details("jimmie")


#Return values
def users(first_name,last_name):
	"""display full name,neatly formatted"""
	full_name=f"\n {first_name} {last_name}"
	return full_name.title()

name_of_user=users("yash","vendra")
print(name_of_user)

#avoiding arguments
def users(first_name,last_name,middle_name=""):	#here we make middle name as optional by defining it as empty string
	"""display full name,neatly formatted"""
	if middle_name:
		full_name=f"\n {first_name} {middle_name} {last_name}"
	else:
		full_name=f"\n {first_name} {last_name}"
	return full_name.title()	


name_of_user=users("yash","vendra")
print(name_of_user)

name_of_user=users("yaswanth","vendra","sai")
print(name_of_user)

#
def person_info(first_name,last_name,age=None):    #age is an optional argument 
	full_name = {"first":first_name,"last":last_name}
	if age:                                        #in conditional statements, None evaluates to false
		full_name["age"]=age
	return full_name

message = person_info("yash","vendra",17)
print(message)

#arbitary arguments(accepts any no. of arguments)
def friends(*frnds):       #asterisk term accepts any no. of arguments and creates a tuple with them
	"""create a frnds list"""
	print(frnds)
friends("sai")
friends("yash","sai","vendra")

def friends(*frnds):
	"""create a frnds list"""
	for frnd in frnds:
		print(frnd)
print("frnds_list: ")
friends("sai","yash","vendra")

#when using arbitary arguments with positional or keyword arguments,place arbitary arguments at end
#arbitary with positional arguments:
def pizza(size,*toppings):
	"""making a pizza"""
	print(f"size_of_pizza={size}")
	print("toppings: ")
	for topping in toppings:
		print(topping)
order=pizza(40,"cheese","chilli","peas")
print(order)
#arbitary keyword arguments:
def user(first_name,last_name,**user_info):
	"""creating a dictionary with user information"""
	user_info["f_name"]=first_name
	user_info["l_name"]=last_name
	print(user_info)
user("yash","vendra",address="12-52",street="vendra vari street")




# Docstring
# Docstrings are multi-line comments which acts as a short descriptions for functions, classes, methods and modules.
# They should be placed at the start of the code block.

def doc_str_fun():
	"""this is a docstring
		this function helps us to understand docstring.
	"""
	print("docstring function")
#In most of the IDEs, one can hover over the function to see the docstring, so that they can quickly get an idea on how the function works.
doc_str_fun()
#one can use .__doc__ method to view the docstring.
print(doc_str_fun.__doc__)

#We can even use this __doc__ dunder method to view the docstrings of built-in fucntions.
import math
print(math.__doc__)
print(math.sqrt.__doc__)
		
		






