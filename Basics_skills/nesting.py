#Nesting
#1.nest dictionaries into a list
alien1 = {"color":"green","points":5}
alien2 = {"color":"green","points":15}
alien3 = {"color":"green","points":10}
aliens=[alien1 ,alien2,alien3]
for alien in aliens:
	print(alien)
#example to create 30 aliens:
aliens = []
for alien_num in range(30):			#here range just helps the loop to repeat 30 times.
	new_alien = {"color":"green","points":10}
	aliens.append(new_alien)
print(len(aliens))
#2.nest lists into a dictionary
pizza={
	"crust":"thick",
	"toppings": ["cheese","chilli"]
    }
#nest a dictionary into a dictionary




	
   


