# __init__() Method

# All classes have a built-in method called __init__(), 
# which is always executed when the class is being initiated.


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)



# Without the __init__() method, you would need to set properties manually for each object
class Person:
  pass

p1 = Person()

p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)



# Set default value in the __init__() method
class Person:
  def __init__(self, name="anonymous", age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)
p3 = Person()
print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)





# self Parameter

# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()
# output: Hello, my name is Emil




# Access a property with self
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()
# output: 2020 Toyota Corolla





# Calling Methods with self
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome() 
# Hello, Tobias! Welcome to our website.





