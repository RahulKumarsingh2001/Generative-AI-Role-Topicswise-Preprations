def calculate(a, b):
    return a + b, a - b, a * b

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)

#return a + b, a - b, a * b returns one tuple containing three values. 
# Python unpacks that tuple into the three variables.




# Types of functions -> Inbuilt , User-defined, Anonymous (lambda) functions

square = lambda n: n * n
print(square(5))


students = [
    ("Aman", 85),
    ("Priya", 92),
    ("Rahul", 78)
]
result = sorted(students, key=lambda std: std[1])
print(result)



# rucursion
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)

fact =factorial(5)
print(fact)

# TODO: if we not add base case then it will run until it reaches maximum depth of recursion
#.      and then it throws RecursionError







def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))  # Output: ['apple']
print(add_item("banana"))  # Output: ['apple', 'banana']




# passing a function as a argument to another function
def square(n):
    return n*n

def apply(fun, n):
    return fun(n)

print(apply(square, 5))




#  Higher-order functions
# A higher-order function takes another function as an argument, returns a function, or does both.

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*2, numbers))
print(result)




# closure
def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))




# Docstrings :- it describes what the function does.
def square(number: int) -> int:
    """Return the square of an integer."""
    return number * number

print(square.__doc__) # Output: Return the square of an integer.