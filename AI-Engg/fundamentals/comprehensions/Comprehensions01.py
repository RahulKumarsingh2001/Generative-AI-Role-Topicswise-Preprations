# Python Comprehensions
# In Python, comprehensions provide a concise way to create a new list, 
# set, dictionary, or generator from an existing iterable using a single expression.




# List Comprehension:- List comprehension creates a new list in a single line.
# syntax: [expression for item in iterable]


from ast import List


numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)





# create a square of numbers
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)






# List compression with if condition
numbers = [1, 2, 3, 4, 5]
evensquare = [n**2 for n in numbers if n%2 == 0]
print(evensquare)





# List compression with if-else condition
numbers = [1, 2, 3, 4, 5]
result = ["Even" if n**2 == 0 else "Odd" for n in numbers]
print(result)
    
    
    
    
    



# Dictionary Comprehension:- Dictionary comprehension creates a dictionary using key-value pairs.
# syntax: {key_expression: value_expression for item in iterable}



# Create a number-to-square dictionary
numbers = [1, 2, 3, 4, 5]
squares = {n: n ** 2 for n in numbers}
print(squares)
    
    
# filter a dic
scores = {
    "Rahul": 85,
    "Amit": 45,
    "Priya": 92
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 50
}

print(passed) # {'Rahul': 85, 'Priya': 92}    








# Set Comprehension:- Set comprehension creates a set, which stores unique elements.
# syntax: {expression for item in iterable}

numbers = [1, 2, 2, 3, 3, 4, 5]
unique_squares = {n ** 2 for n in numbers}
print(unique_squares)




# Generator Expression:- A generator expression looks similar to a list comprehension 
#                        but uses parentheses instead of square brackets.


numbers = [1, 2, 3, 4, 5]
squares = (n ** 2 for n in numbers)
for value in squares:
    print(value)
    
    
    
    
# Feature	        List comprehension	                    Generator expression
# Syntax	        [n**2 for n in numbers]	                (n**2 for n in numbers)
# Evaluation	    Creates the list immediately	        Produces values as requested
# Memory	        Stores the resulting list	            Typically uses less memory
# Reusable	        Can iterate over the list repeatedly	A consumed generator does not restart automatically    



