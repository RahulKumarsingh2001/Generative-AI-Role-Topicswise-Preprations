# Generators

# Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.


#Generator functions
# A generator function uses yield to produce values one at a time rather than returning all of them at


def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
  
# Output:  
# 1
# 2
# 3


# yield keyword:-  is what makes a function a generator.
# next() function:- is used to retrieve the next value from a generator object.

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))


# send() method allows you to send a value to the generator:

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")
# Output:
# Received: Hello
# Received: World





# close() method stops the generator
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()
# output:
# 1
# Generator closed