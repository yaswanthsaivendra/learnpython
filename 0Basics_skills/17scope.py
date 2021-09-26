#scope - local and global variables.
# A global variable can be used anywhere in that module namespace.
global_var=1

def fun():
	print(global_var)
	return
fun()
# A variable declared inside a function and classes are local variables.

def fun():
#a local variable cannot be used in global scope but a global variable can be used in local scope
	local_var=4	
	return
fun()
#print(local_var)	#this give an error, as we are trying to use local variable in global scope.

# Local variables are given more preference than global variable.(within the scope of a local variable).
var=4
def fun():
	var=5
	print(var)	#value of local variable will be printed.
	return
fun()

# Normally, we can access a global variable inside local scope but we cannot make permanent changes to it.
# If we want to make changes to global varaible under local scope, we use global keyword.
# u may think like what cant we create a variable using the same name inside the function but its going to another variable just with the same name. So we use global keyword to make that normal local variable as already created global variable with the same name.

def fun():
	global eggs      #global statement
	eggs=10

eggs=20
fun()
print(eggs)

# Avoid using global, wherever possible.


# Nonlocal Variables
# Nonlocal variables are used in nested functions. These variables can be neither in the local nor the global scope.
# They act as , they are in the local scope of outer function.

def outer():
	x= "local"

	def inner():
		nonlocal x;
		x="nonlocal"	#here this, nonlocal variable acts as the local variable of outer function.
		print("inner:", x)

	inner()
	print("outer: ",x)

outer()
