# A set in Python is a collection of unique elements. 
# It automatically removes duplicate values and does not support indexing like lists or tuples.


# creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers) # {1, 2, 3, 4, 5}



# remove duplicate elements 
numbers = {1, 2, 2, 3, 3, 4}
print(numbers) # {1, 2, 3, 4}




# creating a empty set
a = set()
print(type(a)) # <class 'set'>



# unique property of sets
# Unique elements, unordered collection, mutable, no indexing, no duplicates






# Method	        Purpose
# add(x)	        Adds one element
# update(iterable)	Adds multiple elements
# remove(x)	        Removes an element; raises KeyError if absent
# discard(x)	    Removes an element without an error if absent
# pop()	            Removes and returns an arbitrary element
# clear()	        Removes all elements
# copy()	        Creates a shallow copy





numbers = {1, 2, 3}

numbers.add(4)
numbers.update([5, 6])
numbers.discard(2)

print(numbers) # {1, 3, 4, 5, 6}



# What is the difference between remove() and discard()?
# - remove() raises KeyError if the element does not exist.
# - discard() does not raise an error if the element does not exist.






# Mathematical Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B) # {1, 2, 3, 4, 5, 6}
print(A.union(B)) # {1, 2, 3, 4, 5, 6}

# Intersection
print(A & B) # {3, 4}
print(A.intersection(B)) # {3, 4}

# difference
print(A - B) # {1, 2}
print(A.difference(B)) # {1, 2}

# Symmetric difference:- Returns elements present in either set, but not both.
print(A ^ B) # {1, 2, 5, 6}






# Membership Testing
numbers = {10, 20, 30, 40}

print(20 in numbers)
print(50 in numbers)







# Frozen Sets:- A frozenset is an immutable version of a set.

numbers = frozenset([1, 2, 3])

print(numbers)
# you cant add or remove elements from a frozenset






# set not conatin list





A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B)) # True
# it can check all set contain unique elements or not