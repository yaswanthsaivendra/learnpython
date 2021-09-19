#tuples - these are the lists that cannot be changed.
dimensions = (30,40)#we use parenthesis instead of square brackets
print(dimensions)
#we can't change a value in tuples but we can rewrite the tuples..
dimensions = (40,50)
for dimension in dimensions:
    print(dimension)


# set(it differs from dictionary as dict contains key-values)
lang = {"c", "python", "java", "python"}
print(lang)  # return elements uniquely