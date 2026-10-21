# A generator in Python is a special type of iterator that produces values 
# one at a time instead of storing all values in memory at once.



# Normal function
def get_numbers():
    return [1, 2, 3, 4, 5]

numbers = get_numbers()
print(numbers)
# output: [1, 2, 3, 4, 5]




# generator
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()

print(next(numbers)) # 1
print(next(numbers)) # 2
print(next(numbers)) # 3




# return finishes a function
# yield pauses a function and allows it to resume later.




