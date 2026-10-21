# File handling in Python allows you to create, read, write, append, and modify files using Python code.




# Mode	    Meaning	                Behavior
# "r"	    Read	                Reads an existing file
# "w"	    Write	                Creates a file or overwrites existing content
# "a"	    Append	                Adds content to the end
# "x"	    Create	                Creates a new file; fails if it exists
# "rb"	    Read binary	            Reads binary data, such as images
# "wb"	    Write binary	        Writes binary data
# "r+"	    Read and write	        Reads and writes without truncating initially



# What is the difference between "w" and "a"?
# "w" replaces existing content.
# "a" preserves existing content and adds new content at the end.





# opening files
file = open("data.txt", "r")



# Reading a file

# Using read() :- Reads the entire file as a string.
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    
# Using readline() :- Reads one line at a time.
with open("data.txt", "r") as file:
    print(file.readline())
    print(file.readline())    

    
# Using readlines() :- Returns all lines as a list.
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    
    
    
    
# Writing to a file
with open("data.txt", "w") as file:
    file.write("Hello Python")


with open("data.txt", "w") as file:
    file.write("Python\n")
    file.write("Generative AI\n")    
            
            

# Appending to a file
with open("data.txt", "a") as file:
    file.write("\nLearning File Handling")
    
    
    
    
    
    
    
# Why use with open()?

# without "with"
file = open("data.txt", "r")
print(file.read())
file.close()


# with "with"                
with open("data.txt", "r") as file:
    print(file.read())
    
# The with statement automatically closes the file when the block finishes,







# Checking whether a file exists
from pathlib import Path

file_path = Path("data.txt")

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")
    
    
    
    
    
# Working with file paths
# The pathlib module makes file paths easier to manage.
from pathlib import Path

file_path = Path("data") / "notes.txt"

print(file_path)
# This constructs a path to notes.txt inside the data directory using 
# the appropriate path separator for the operating system.        







# To create a directory
Path("data").mkdir(parents=True, exist_ok=True)
# parents=True creates missing parent directories.
# exist_ok=True avoids an error if the directory already exists.






# File pointer: seek() and tell()
# Python tracks the current position within an open file.
# - tell() returns the current position.
# - seek() moves the position.

with open("data.txt", "r") as file:
    print(file.tell())  # 0

    print(file.read(5))  # Reads 5 characters

    print(file.tell())  # Position after reading

    file.seek(0)        # Return to the beginning

    print(file.read(5))