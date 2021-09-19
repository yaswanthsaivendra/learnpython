#we can turn a local variable into global variable by using a global statement.
def fun():
	global eggs      #global statement
	eggs=10

eggs=20
fun()
print(eggs)

#a local variable cannot be used in global scope but a global variable can be used in local scope
