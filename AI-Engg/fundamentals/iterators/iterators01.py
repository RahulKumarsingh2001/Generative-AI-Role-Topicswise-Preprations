# iterator in Python is an object that allows you to access elements 
# one at a time, rather than accessing all elements at once.


numbers = [10, 20, 30, 40]
for number in numbers:
    print(number)
    
    
# iter() and next()

# Python provides two important built-in functions for working with iterators.
# - iter() — creates an iterator from an iterable.
# - next() — retrieves the next element from an iterator.    
numbers = [10, 20, 30, 40]
iterator = iter(numbers)
print(next(iterator)) # 10
print(next(iterator)) # 20
print(next(iterator)) # 30
print(next(iterator)) # 40







numbers = [10, 20]
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break