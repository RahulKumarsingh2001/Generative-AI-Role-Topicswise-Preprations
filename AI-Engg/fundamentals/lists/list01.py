# A list in Python is an ordered, mutable collection that can store multiple items in a single variable. 
# Lists can contain duplicate values and different data types.

# Lists are one of the most important Python topics for coding interviews and Generative AI engineering.




numbers = [10, 20, 30, 40, 50]

print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[-1])  # 50
print(numbers[-2])  # 40



# List Slicing:- list[start:stop:step]

# reverse a list
numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]


# list are mutiable so we can change the values of a list
numbers = [10, 20, 30, 40, 50]
numbers[0] = 100
print(numbers)  # [100, 20, 30, 40, 50]
numbers[1:3] = [200, 300]
print(numbers)  # [100, 200, 300, 40, 50]





# some list methods
# append() --> add an item to the end of the list
# extend(iterable) --> add all items from an iterable to the end of the list
# insert(index, item) --> insert an item at a specific index
# remove(item) --> remove the first maching value from the list
# pop(index) --> remove and return an item at a specific index
# clear() --> remove all items from the list
# index(item) --> return the index of the first matching value
# count(item) --> count the number of occurrences 
# sort() --> sort the items of the list in ascending order
# reverse() --> reverse the order of the items in the list
# copy() --> return a shallow copy of the list






a = [1,2]
a.append([3,4]);
print(a) # [1, 2, [3, 4]]

a = [1,2]
a.extend([3,4])
print(a) # [1, 2, 3, 4]



# sort() -> modifie the original list and return None
# sorted() -> return new shorted list


numbers = [10, 20, 30]
for num in numbers:
    print(num)
# 10
# 20
# 30    
    
for i in range(len(numbers)):
    print(i, numbers[i]) 
# 0 10
# 1 20
# 2 30       
    
for index, value in enumerate(numbers):
    print(index, value)    
# 0 10
# 1 20
# 2 30       




# List Comprehension
# List comprehension provides a concise way to create a new list.

# syntax: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]
square = [x**2 for x in numbers]
print(square)  # [1, 4, 9, 16, 25]