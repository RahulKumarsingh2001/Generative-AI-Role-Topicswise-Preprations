# Python Dictionaries 
# A dictionary in Python is a built-in data type that stores data in key-value pairs.


# creating a dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

print(student)



# access a dict
print(student["name"])
print(student["age"])

print(student.get("name"))       # Rahul
print(student.get("city"))       # None



# What's the difference between [] and get()?

# student["city"] raises a KeyError if the key doesn't exist.
# student.get("city") returns None by default if the key doesn't exist.




# Adding and update a Elements
student = {
    "name": "Rahul",
    "age": 22
}
student["city"] = "Bengaluru"

print(student)




# removing a elements
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Bengaluru"
}
del student["age"]
city = student.pop("city")
item = student.popitem() # Remove and return the last inserted key-value pair
student.clear()  # Removes all entries
print(student)





# Method	    Purpose

# keys()	    Returns the dictionary's keys
# values()	    Returns the dictionary's values
# items()	    Returns key-value pairs
# get(key)	    Safely retrieves a value
# update()	    Adds or updates multiple entries
# pop(key)	    Removes a key and returns its value
# popitem()	    Removes the last inserted pair
# setdefault()	Returns a value or inserts a default
# clear()	    Removes all entries
# copy()	    Creates a shallow copy


student = {"name": "Rahul", "age": 22}

print(student.keys()) # dict_keys(['name', 'age'])
print(student.values()) # dict_values(['Rahul', 22])
print(student.items()) # dict_items([('name', 'Rahul'), ('age', 22)])






# iterate
for key, value in student.items():
    print(key, value)
    
    

# checking if a key exists
student = {"name": "Rahul", "age": 22}
print("name" in student)  # True
print("city" in student)  # False  
print("Rahul" in student.values())  # True





# Dic have some rules:

# Rule 1: Keys must be hashable
# Strings, integers, and tuples containing only hashable elements can be dictionary keys.
data = {
    "name": "Rahul",
    10: "Ten",
    (1, 2): "Tuple key"
}
# Rule 2: Keys must be unique

# Rule 3: Values can be of different types
data = {
    "name": "Rahul",
    "age": 22,
    "marks": [80, 90, 95],
    "active": True,
    "details": {"city": "Bengaluru"}
}

# Rule 4: Dictionaries preserve insertion order

# Rule 5: Dictionaries are mutable





# Iterating Through a Dictionary
scores = {
    "Python": 90,
    "Java": 85,
    "JavaScript": 88
    }

# Iterate through keys
for key in scores:
    print(key)

# Iterate through values
for value in scores.values():
    print(value)

# Iterate through key-value pairs
for key, value in scores.items():
    print(f"{key}: {value}")
  
  
  
  
  
  
  

# Dictionary Comprehension
# A dictionary comprehension creates a dictionary in a concise way.

even_squares = {
    n: n ** 2
    for n in range(1, 11)
    if n % 2 == 0
}

print(even_squares) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}







# Nested Dictionaries
students = {
    "student1": {
        "name": "Rahul",
        "age": 22
    },
    "student2": {
        "name": "Amit",
        "age": 23
    }
}

print(students["student1"]["name"])  