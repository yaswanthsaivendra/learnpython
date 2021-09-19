#In programming, a module is a piece of software that has a specific fucntionality.
#In python, a module is simply a python file with .py extension.
#the name of module will be name of the file(without considering extension).


#importing  entire module
import module               #after reaching this line, python interpreter looks for the module.py file in current directory, if it find a one, it will import the file. If not, then it will look for the file in built-in library.
module.fun_name("yash","vendra")    #we use the function of the module using dot operator.

#importing specific functions from a module
from module import fun_name
fun_name("yash","vendra")   #here we imported the particular function into current namespace, so no need to use dot operator.

#using 'as' to give a function an alias
from module import fun_name as f
f("yash","vendra")

#using 'as' to give a module an alias
import module as m
m.fun_name("yash","vendra")

#importing all functions in a module
from module import *    #not a good practice.
fun_name("yash","vendra")

#when we use imports in our python programs, a .pyc file will be created under __pycache__ directory in our current directory. It is nothing but bytecode of the modules loaded.(similar to object file in c)

#Extending module load path :
#we can set an env variable PYTHONPATH to specify additional directories to look for modules.(PYTHONPATH=/dir1:/dir2)
#other way is to use sys.path.append function before import command.
import sys
print(sys.path) #it lists the directories that python interpreter searches for to load moduels.
sys.path.append("/home/yaswanth/Desktop/python_notes/Basics_skills")
print(sys.path)
#when we are creating working projects, first method is recommended as we cannot predict the path of our enduser.


#Exploring built-in modules.
import os
#when importing built-in modules, the two most useful functions are dir and help.
print(dir(os))  #it lists functions in module.
print(help(os.write))   #it prints help about a particular function.
