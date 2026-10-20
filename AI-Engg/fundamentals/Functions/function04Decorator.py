# Decorator
# let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.



def changecase(func):
    def inner():
        return func().upper()
    return inner


@changecase
def greet():
    return 'Hello, World!'
print(greet())  # Output: HELLO, WORLD!



# arugments in decorator
def changecase(func):
    def inner(x):
        return func(x).upper()
    return inner

def greet(name):
    return f'Hello, {name}!'
print(greet('Alice'))  # Output: Hello, Alice!




# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes
def myfunction():
  return "Have a great day!"
print(myfunction.__name__) # Output: myfunction
print(myfunction.__doc__) # Output: None