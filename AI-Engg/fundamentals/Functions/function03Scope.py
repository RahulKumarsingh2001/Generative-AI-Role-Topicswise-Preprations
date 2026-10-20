# Scope

# Local Scope:- A variable created inside a function is available inside that function only.

def myfunc():
  x = 300
  print(x)

myfunc()


def myfunc():
  x = 300
  def myinnerfunc():
    print(x) 
  myinnerfunc()

myfunc()


# Global Scope:- A variable created in the main body of the Python code is a global variable and belongs to the global scope.
x = 300

def myfunc():
  print(x)
myfunc()

print(x)



# Global Keyword:- if you need to create a global variable, inside a function, you can use the global keyword.
def myfunc():
  global x
  x = 300
myfunc()
print(x)


# Nonlocal Keyword:- if we used a nonlocal keyword, the variable belongs to outer function and not the local function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) # hello 