# exceptions are errors that occur while a program is running and interrupt its normal execution. 
# We use exception handling to prevent unexpected errors from crashing our programs.

a = 10
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
    


# when else Block run? :- Runs only when the try block completes without an exception.
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("Number cannot be zero")

else:
    print("Result:", result)

finally:
    print("Program execution completed")    
    
    
    
    
    
 
 
 
 
# Common Python exceptions 
# Exception	        :-    When it occurs
# ZeroDivisionError	:-    Dividing by zero
# ValueError	    :-    Correct type, but invalid value
# TypeError	        :-    Operation on incompatible types
# IndexError	    :-    List or tuple index is out of range
# KeyError	        :-    Dictionary key does not exist
# NameError	        :-    Using an undefined variable
# AttributeError	:-    Accessing a nonexistent attribute
# FileNotFoundError	:-    Requested file does not exist
# ImportError	    :-    Import cannot be completed
# Exception	        :-    Base class for most ordinary, non-system-exiting exceptions    




# Catching multiple exceptions
try:
    num = int(input("Enter a number: "))
    print(100 / num)
    
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

    
    

# raise keyword
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")

    return "Access granted"

print(check_age(16))    