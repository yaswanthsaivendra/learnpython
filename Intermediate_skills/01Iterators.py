# Iterators in python is simply an object that is used to iterate over objects like lists, tuples, dicts and sets...these are called iterables.
# iterator object implement two methods, __iter__() and __next__(), collectively called iterator protocol.
#we iterate through the elements using next(), when it reaches the end, it will raise the StopIteration Exception.
#we can call dunder methods without underscores as functions . ie., .__iter__() as iter() and .__len__() as len().

l = [1,2,3,4]
iter_obj = iter(l)

print(next(iter_obj))
print(iter_obj.__next__())
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))   #will raise an StopIteration Exception here.

#the same methodology is also used in the for loop internally.
#create an iterator object using iter() and iterating through the elements using next() and finally exciting when StopIteration Exception is raised.
#Internal implementaion of for loop:
iterable=[1,2,3,4,5]
iter_obj=iter(iterable) #here iterable can be anything like list,dict...etc

#infinte loop
while True:
    try:
        #get the next item
        element=next(iter_obj)
        #do something with element(i.e., body of the for loop).
    except StopIteration:
        #if StopIteration is raised, break from loop.
        break

#creating a custom iterator

class Even:
    def __init__(self,max):
        self.n=2
        self.max=max
    
    def __str__(self):
        return "class which generates even numbers which are less than max variable"

    def __init__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result=self.n
            self.n+=2
            return result
        else :
            raise StopIteration

iter_obj=Even(10)
next(iter_obj)
next(iter_obj)
next(iter_obj)

#Iterators are used to work with large streams of data. These large streams of data cannot be stored in memory at once.