#find method (finds the first occurence of string and return its index )
fruit = "banana"
print(fruit.find("na"))
#if the substring is not found,it returns -1
print(fruit.find("z"))
#replace method(its like search and replace)
print(fruit.replace("na","ra"))#replace all occurences of the substring
#startswith method
if fruit.startswith("ba"):
    print("yes")
else:
    print("no")

#An escape character lets you use characters that are otherwise impossible to
#put into a string. An escape character consists of a backslash(\) followed
#by the character you want to add to the string.
print('let\'s play the game')

##Escape character Prints as
##\' Single quote
##\" Double quote
##\t Tab
##\n Newline(line break)
##\\ Backslash

#raw string completely ignores all escape characters 
print(r'it\'s play time')

#multi line strings (triple quotes)
print('''hi all
this is yaswanth vendra

firstly,thank u all for attending the meet

bye''')

#multi line comments (triple quotes)

''''hi all
this is yaswanth vendra

firstly,thank u all for attending the meet

bye'''

#upper and lower methods used to change the case of string
#isupper and islower methods used to check the case of string,returns a boolean(True or False)

"""isalpha() returns True if the string consists only of letters and is not blank.
•	 isalnum() returns True if the string consists only of letters and numbers
and is not blank.
•	 isdecimal() returns True if the string consists only of numeric characters
and is not blank.
isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank.
•	 istitle() returns True if the string consists only of words that begin with
an uppercase letter followed by only lowercase letters."""

"""The startswith() and endswith() methods return True if the string value they
are called on begins or ends(respectively) with the string passed to the
method"""

#join and split method
""">>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon"""

"""    >>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']      """

#rjust(),ljust() and center() methods
"""> 'Hello'.rjust(10)
' Hello'
>> > 'Hello'.rjust(20)
' Hello'
>> > 'Hello World'.rjust(20)
' Hello World'
>> > 'Hello'.ljust(10)
'Hello '"""

#second optional argument for these methods(means fill)
""">> > 'Hello'.rjust(20, '*')
'***************Hello'
>> > 'Hello'.ljust(20, '-')
'Hello---------------'"""



