#exception handling :
#Exception handling - does mean that handling exceptional cases but not syntax errors.
#python have some built-in exceptions and we can raise custom exceptions as well.

#raising an exception
x=10
if x>5:
	raise Exception('x exceeded 5, x should not exceed 5') #program raises an exception and stop at this line without going further.


#AssertionError - Instead fo waiting for the exception, we can assert to check for a statement is true or false and raise an exception if it turns out to be true.

import sys
assert 'linux' in sys.platform, "this code runs on linux only"
#the above runs successfully on linux, but if we run it on any other platform we will get an assertion something like this:
"""
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError: This code runs on Linux only.
"""


#try and except block 
#It continue the program inspite of an error.
"""
try:
	run this code
except:
	excute this when there is an exception.
"""

def fun(divide_by):
	"""divide by function with try and except block"""
	try:
		return 40/divide_by
	except:	#here we used bare except block, but it is not a good practice. It is recommended to catch the exact exception and handle every seperate exception as a seperarte case.
		return "error,zero divison not allowed"
print(fun(4))
print(fun(10))
print(fun(0))    #zero division is an error,even though program runs to next step without stopping here
print(fun(3))

def fun(divide_by):
	"""divide by function with try and except block"""
	try:
		return 40/divide_by
	except ZeroDivisionError as error:	#we handled the exception with the exact exceptional case.
		return error	


print(fun(5))
print(fun(0))
print(fun(4))


#else and finally clauses

"""
try:
	run this code.
except:
	excute this code when there is an exception,
else:
	No exceptions? run this code,
finally:
	always run this code.
"""