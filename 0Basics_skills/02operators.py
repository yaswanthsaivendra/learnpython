#Operators
print(5*2)       #here * acts as multiplication operator
print(5**2)      #its 5 power 2
print(5/2)       #divsion
print(5//2)      #quotient
print(5%2)       #remainder

#here * acts as string replication operator
print("*" * 10)      
print("yash" * 5)

#concatenate - we can only concatenate a str to str and a int to int but we cannot concatenate a str to int 
price = 10
print(10+price)    #int to int      here + acts as addition operator 
name= "yash"
print(name + "sai")   #str to str     here + acts as string conactenation operator
print("\t" + name)


x=2
print(x==2) #prints out True
print(x!=2) #prints out False
print(x<3) #prints out True



#and , or
age = 10  #similarly,we can use or
if (age>7) and (age<12):	#parenthesis are used to increase readability.
	print("you are eligible to participate")

#in(to check whether if it is there or not),not
users=["sai","yash","vendra","raja"]
user = "raja"
if user in users:
	print("welcome!")
user="anu"
if user not in users:
	print("u are'nt registered")
else:
	print("welcome")

#unline "==" operator ,the "is" operator does not match the values of the variables, but the instances itself.
x=[1,2]
y=[1,2]
print(x is y)   #prints out False
print(x==y)   #prints out True