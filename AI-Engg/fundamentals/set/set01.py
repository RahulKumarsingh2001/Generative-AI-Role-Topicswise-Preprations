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