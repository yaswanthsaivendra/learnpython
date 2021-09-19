# collection of key-value pairs in curly braces is called a dictionary.
# every key is associated with its value.. a value can be a string,number,dictionary or anything(basically any object).
dictionary = {"sai": "topper", "marks": 98}

# we can access value by its key ex: nameofdictinary[key]
print(dictionary["sai"])
print(dictionary["marks"])

alien = {"color": "green", "points": 5}
print(alien)
alien["x_position"] = 0  # adding coordinates to the position of alien
alien["y_position"] = 20
print(alien)

# we can remove key-value pairs by using del statement.
del alien["points"]
print(alien)

# large dictionaries-we can use dictionaries eitheir for storing same kind of data of different members or to store all data of single member.
fav_langs = {
    "john": "c",
    "yash": "python",
    "sai": "java",
    # adding a comma at end will benfits us when we add another key-value.
    "vendra": "kootlin",
}
print(fav_langs["yash"].title())

# using get method will prevent from getting an error due to absence of requested key value.
# here first argument is key & second argument is the one which is to be printed on screen if the key is not present,instead of showing an error.
print(fav_langs.get("anu", "anu key-value is not assigned"))
# here second argument is optional,if it is not given then ...none...will be printed(means no value exist)

# looping through a dictionary:
# items method
for name, lang in fav_langs.items():
    print(f"fav lang of {name} is {lang}")
# keys method(to access only keys)
for name in fav_langs.keys():
    print(name)

# values method(to access only values)
fav_langs = {
    "john": "c",
    "yash": "python",
    "sai": "java",
    "vendra": "python",
}
for lang in fav_langs.values():
    print(lang)



