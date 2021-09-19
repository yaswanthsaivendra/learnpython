#if elif
age=int(input("enter ur age: "))	#input function returns a str, so we should cast to into integer using int() function.
if age<=4 :
	price=0
elif age>4 and age<20:			#we can omit else condition.
	price=50					#sometimes it is better to omit else condition and use elif to particularly mention and use the condition to avoid any minor errors 
elif age>20:						 
	price=200
print(f"u must pay {price} as entry fee")


#pass statement(it is used in loops inspite of actual code and can write the actual code in the future)
#inspite of leaving it blank we use the pass statement to avoid errors while running it.

num =3
if num >0:
    pass