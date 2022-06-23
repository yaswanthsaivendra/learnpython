#lambda(anonymous) fucntions.  

#lambda fucntion to return the doubled value of an integer.
double = lambda x:x*2   # lambda paramter1,paramter2 : Expression_to_be_returned.
print(double(10))

#These ambda functions dont have any name, so we call them anonymous functions.
#lambda function to retrun larger of two numbers.
larger = lambda a,b: a if a>b else b
print(larger(10,47))


#lambda functions are mostly used along with built-in fucntions of python. one of the use case:
names=["sai","raja","bob","alice","anu","james"]
#names will be sorted based on the length.
#sort method takes two optional paramters.
names.sort(key= lambda x:len(x))    # .sort(reverse= True|False, key=myfunc)
print(names)
