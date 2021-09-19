#exception handling :
#try and except block (used to continue the program inspite of an error)
def fun(divide_by):
	"""divide by function with try and except block"""
	try:
		return 40/divide_by
	except:
		return "error,zero divison not allowed"
print(fun(4))
print(fun(10))
print(fun(0))    #zero division is an error,even though program runs to next step without stopping here
print(fun(3))



