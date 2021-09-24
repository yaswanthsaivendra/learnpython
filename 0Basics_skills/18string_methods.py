#find method (finds the first occurence of string and return its index )
fruit = "banana"
print(fruit.find("na"))
#if the substring is not found,it returns -1
print(fruit.find("z"))

#replace method(its like search and replace)
print(fruit.replace("na","ra"))#replace all occurences of the substring


#startswith and endswith methods
if fruit.startswith("ba"):
    print("yes")
else:
    print("no")
if fruit.endswith("na"):
    print("yes")
else:
    print("no")


#escape character :
print('let\'s play the game')
##Escape character Prints as
##\' Single quote
##\" Double quote
##\t Tab
##\n Newline(line break)
##\\ Backslash


#upper and lower methods used to change the case of string.
print("LOWer".lower())
print("uppER".upper())
#title() method.
print("TITLE".title())  #first letter will be uppercase and remaining all will be lowercase.

#isupper and islower methods used to check the case of string,returns a boolean(True or False).
#Similarly , istitle().


#join method    
print(', '.join(['cats', 'rats', 'bats']))

print(' '.join(['My', 'name', 'is', 'Simon']))

#split method.
print('My name is Simon'.split())

print('MyABCnameABCisABCSimon'.split('ABC'))






