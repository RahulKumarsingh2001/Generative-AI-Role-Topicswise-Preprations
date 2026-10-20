# What is *args?

# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple 



# Arbitrary Arguments - *args
def my_function(*args):
  print("Type:", type(args))   # tuple 
  print("First argument:", args[0]) # Email
  print("Second argument:", args[1]) # Tobias
  print("All arguments:", args) # ('Emil', 'Tobias', 'Linus')

my_function("Emil", "Tobias", "Linus")




def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
# OutPut:
# Hello Emil
# Hello Tobias
# Hello Linus






# Arbitrary Keyword Arguments - **kwargs

# if we don't know how many keywords args will be passed to your function


def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")  # His last name is Refsnes



def my_function(**myvar):
  print("Type:", type(myvar))  # dict
  print("Name:", myvar["name"]) # Tobias
  print("Age:", myvar["age"]) # 30
  print("All data:", myvar) # {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}
my_function(name = "Tobias", age = 30, city = "Bergen")




def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# Username: emil123
# Additional details:
# age: 25
# city: Oslo
# hobby: coding






# unpack list with * 
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) # 6




# Unpacking Dictionaries with **
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
# Output: Hello Emil Refsnes