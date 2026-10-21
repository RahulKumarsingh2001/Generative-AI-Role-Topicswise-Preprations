# Mutability
# Mutability means whether an object can be changed after it has been created.


# Mutable objects -> Lists, dictionaries, sets.
numbers = [1, 2, 3]
numbers[0] = 100
print(numbers)  # [100, 2, 3]


# Immutable objects:- Integers, floats, strings, tuples, booleans.
name = "Rahul"
name = name + " Singh"
print(name)  # Rahul Singh



