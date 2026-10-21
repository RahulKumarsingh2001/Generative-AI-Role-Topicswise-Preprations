# Python Tuples — 
# A tuple in Python is an ordered collection of elements that is immutable, 
# meaning you cannot modify its elements after creating it.

# Tuples are useful when you want to store multiple values together and keep them unchanged.



# Tuple of integers
from ast import List, Not, Tuple


numbers = (10, 20, 30, 40)

# Tuple of strings
names = ("Rahul", "Aman", "Priya")

# Tuple with different data types
data = (10, "Python", 3.14, True)

print(numbers)
print(names)
print(data)





# Maintain a element order
# element cannot be modefied
# duplicate allowed
# support a positive and negative indexing


numbers = (10, 20, 30, 40, 50)

print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[-1])  # 50
print(numbers[-2])  # 40




# Tuple slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])  # (20, 30, 40)
print(numbers[:3])   # (10, 20, 30)




# inside a tuple any list are present then we can modify the list but we cannot modify the tuple
my_tuple = (1, 2, [3, 4])
my_tuple[2][0] = 30
print(my_tuple)  # (1, 2, [30, 4])

# why this is work?
# see tuples always refer to same list. list container changed but tuple element did not 





# count() --> return how many time that element is occurred
numbers = (10, 20, 30, 40, 50, 10, 20, 10)
print(numbers.count(10))  # 3

# index() --> return the index of the first matching value




a = (10)
b = (10,)

print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>
empty = ()
print(type(empty))  # <class 'tuple'>




# Tuple packing -> putting multiple variable in one tuple
person = "Rahul", 22, "India"

print(person)
# ('Rahul', 22, 'India')


# Tuple unpacking -> extracting values from a tuple into variables
person = ("Rahul", 22, "India")
name, age, country = person
print(name)     # Rahul
print(age)      # 22
print(country)  # India



# uses of * 
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50







# Tuple vs List

# Feature	                         Tuple	                    List
# Syntax	                         (1, 2, 3)	                [1, 2, 3]
# Mutable	                         No	                        Yes
# Add/remove elements	             Not directly	            Yes
# Methods	                         Few	                    Many
# Hashability	                     Depends on its contents	Unhashable
# Typical use	                     Fixed collections	        Collections that change



 
# when we used tuples?
# if we want your data was fixed and unchanged
rgb_color = (255, 0, 0)





# itterate a tuple
number = (10,20,30,40,50)
for num in number:
    print(num)
    
for i, val in enumerate(number):
    print(i, val)

        