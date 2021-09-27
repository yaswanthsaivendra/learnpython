# A decorator takes in a function, adds some functionality to it and returns it.
# Any object, which implements .__call__ dunder method are callable. for ex, methods and fucntions are callable.
# So, a decorator is a callable that returns a callable.

def make_pretty(func):  #Here make_pretty is a decorator, which takes in a function as argument.
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("Iam ordinary")

#make_pretty function(i.e., decorator) acts as wrapper to ordinary function and decorates it.
pretty=make_pretty(ordinary)
pretty()


# We can make this wrapper representation much simpler by using @decorator_name before the ordinary fucntion.

@make_pretty
def ordinary():
    print("Iam ordinary")
ordinary()

#is same as

def ordinary():
    print("Iam ordinary")
ordinary=make_pretty(ordinary)
ordinary()


#using decorators on fucntion which takes in parameters.
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(4,2)

#chaining decorators in python

def star(func):                 #decorator 1
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):                 #decorator 2
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

##using decorators on the fucntion
@star
@percent
def printer(msg):
    print(msg)

printer("Hello")


#the above "using decorator"  code is exactly equivalent to
def printer(msg):
    print(msg)
printer = star(percent(printer))