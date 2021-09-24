#python is completely object oriented, Even a varible in python is a object.
#so we can directly use them without declaring.

#Numbers
#python support three types of numbers - integers, floating point numbers, complex numbers.

#int
myint = 6
print(myint)

#float 
myfloat = 7.0
print(myfloat)


#strings
# we can define either with a single quote or double quotes.

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring="""
hello 
this 
is multiline string!
"""
print(mystring)

#when to use single quotes and when to use double quotes.
#when our sentence contains single quote use double quotes & vice versa
# example :
mystring="I'm learning python"
print(mystring)


"""
Prefix	Base
0b/0B 	Binary	2
0o/0O 	Octal	8
0x/0X 	Hexadecimal	16
"""
print(0o10)
print(0x10)

""" Boolean
False
True
"""

# Type conversion
#1 . Implicit type conversion
int_num=4
float_num=4.2

total=int_num+float_num #before adding, python converts int_num to float data type.

#2. Explicit type conversion.
# For Explicit type conversion, we use built-in functions like int(), float() and str() to convert one data-type to other.
int_num=4
float_num=float(int_num) 
print(type(float_num))  #type() fucntion returns the class of the object.

# During Type conversion,
# we may get errors, if that particular conversion is not possible.
# we may loss data during conversion.