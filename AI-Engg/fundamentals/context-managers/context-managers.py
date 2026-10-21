# A context manager in Python is a mechanism that manages 
# resources automatically by handling setup and cleanup operations.

# Context managers are commonly used for:
# - File handling
# - Database connections
# - Locks and thread synchronization
# - Network connections
# - Managing temporary resources




# without context manager
file = open("data.txt", "w")
try:
    file.write("Hello, Python!")
finally:
    file.close()
    
    
# Using a context manager
with open("data.txt", "w") as file:
    file.write("Hello, Python!")
# Python automatically closes the file when execution leaves the with block, including when an exception occurs.





# How context managers work internally
# A class-based context manager typically implements two special methods:
# - __enter__() — performs setup and returns the object to use inside the block.
# - __exit__() — performs cleanup when the block ends, including when an exception occurs.    



class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


with MyContextManager() as obj:
    print("Inside the context")
    
# Output:-
# Entering the context
# Inside the context
# Exiting the context    


# Argument	    Meaning
# exc_type	    Exception class, or None if no exception occurred
# exc_value	    Exception instance, or None
# traceback	    Traceback object, or None







# Creating context managers using contextlib
# Python provides the built-in contextlib module, which makes it possible to 
# write context managers using a generator and the @contextmanager decorator.



from contextlib import contextmanager

@contextmanager
def my_context():
    print('setup')
    try:
        yield "hello"
    finally:
        print('cleanup')

with my_context() as value:
    print(value)        
    
    
    
    
    
    
    
# Lock management            
from threading import Lock
lock = Lock()
counter = 0

with lock:
    counter += 1

# The lock is released when the block exits, preventing a lock from remaining acquired because of an exception.    