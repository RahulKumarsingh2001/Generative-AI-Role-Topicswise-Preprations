# A module in Python is a file containing Python code, such as functions, variables, and classes, 
# that you can reuse in another Python file.
# Modules help you organize code, avoid repetition, and build maintainable applications.



#Import a specific function
import math

print(math.sqrt(25))
print(math.pi)



#Import using an alias
import random as r

print(r.randint(1, 10))



#Import multiple functions
from math import sqrt, factorial

print(sqrt(49))
print(factorial(5))




# The __name__ == "__main__" condition
def greet():
    print("Hello!")

if __name__ == "__main__":
    greet()




# Feature	        Module	                        Package
# Meaning	        A Python file	                A directory organizing modules
# Example	        calculations.py	                expenses/
# Contains	        Functions, classes, variables	Usually multiple modules and possibly subpackages
# Import example	import calculations	            from expenses import calculations



