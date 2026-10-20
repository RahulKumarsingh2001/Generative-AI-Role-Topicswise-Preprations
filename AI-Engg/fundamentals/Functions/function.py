# normal function
def my_function():
  print("Hello from a function")

my_function()




# return function
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


# pass statements
def my_function_pass():
  pass

# pass statements tells rightnow we want this function 
# in future we need then we can write a code



# function with arguments
def my_function(fname):   # fname is a parameter 
  print(fname + " Refsnes") 

my_function("Emil") # Emil is an argument


# default parameter value
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function()


# keyword arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")




# Positional arguments -> when you call a function with arg without using keywords.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")




# retrn different data types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])




# function return a tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)



# Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
my_function(name = "Emil") # ❌ this will raise an error because name is a positional-only argument



# Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
my_function("Emil") # ❌ this will raise an error because name is a keyword-only argument