names = ["sai","raja","yash","vendra"]
for name in names:#this line tells the python to pull a name from list and associate it with the variable name
	print(name)
#example:
names = ["sai","raja","yash","vendra"]
for name in names:
	print(f"{name},welcome to python!\n")#\n - for a line break,\t - for a tab space

for i in range(5):	#i value changes from 0 to 4. this loop runs 5 times.
	print(i)
for i in range(1,5):	#i value changes from 1 to 4. this loop runs 4 times.
	print(i)
for i in range(1,10,2):	#i value changes from 1 to 10 with difference of 2(i.e., 1,3,5,7,9). 
	print(i)

	


#The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as,or while, a certain condition is true. 
#while loop
prompt = "whatever u say!,i will repeat it for u"
prompt+="otherwise enter quit,to exit the program: "
message=""	#we have to intialize before comparision, so rather we prefer second program mentioned below using flags.
while message != "quit":
	message = input(prompt).lower()
	if message!="quit":
		print(message)


# flags - variable which is used when mutiple cases lead to same output,inspite of all those cases.
prompt = "whatever u say!,i will repeat it for u"
prompt+="  otherwise enter quit,to exit the program: "
active = True	
while active :
	message=input(prompt).lower()
	if message=="quit":
		active=False
	else:
		print(message)

#break(breaks completely from the loop and stops the loop to operate)
#continue(jumps from the loop to the begining without executing the code after the continue statement to execute)

