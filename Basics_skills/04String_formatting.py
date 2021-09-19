#string formatting

## 1. old style string formatting(% operator)
#it is similar to using format specifiers in c.
name = "yash"
print("hello i'm %s" %name)

""" format specifiers
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
"""
age=18
#multiple values by order(uses a tuple)
print("hello i am %s and i am %d" %(name,age) )

#multiple values by name mapping(uses a dictionary)
print("hello i am %(name)s and i am %(age)d" %{"name":name, "age":age} )
#its a better pracitce than above mentioned one, coz its easier to maintain in future.




## 2. new style string formatting(str.format)
print("hello i'm {}".format(name)) #in order.

#we can use them in any order
print("hello i'm {name} and i'm {age}".format(name=name,age=age))




## 3. f-strings(python 3.6+)
print(f'hello i am {name}')
#in f-strings, we can embed arbitary pthon expressions and can even do inline arithmetic.
a = 5
b = 10
print(f"the sum is {a+b}")



## 4. Template strings(standard library)
#this is safer method(avoid security issue), so this should be used when taking user input.
from string import Template
t= Template('Hi i am $name')
t.substitute(name=name)
print(t)

templ_string="hi i am $name and i am $age"
Template(templ_string).substitute(name=name, age=age)



""" Among the 4, which one should be used and when
if user-supplied strings== True:
    use Template Strings
else:
    if python3.6+ == True:
        use f-strings
    else :
        use str.format

"""


