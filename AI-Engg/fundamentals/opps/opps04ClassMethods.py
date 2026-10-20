# class Methods 
# Methods are functions that belong to a class. They define the behavior of objects created from the class.

class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("Hello, my name is " + self.name)
        
p1 = Person("jack")
p1.greet() 
# output: Hello, my name is jack



# Method with parameters
class calculator:
    def add(self, a, b):
        return a + b
    
c1 = calculator()
print(c1.add(5, 3));




# Method accessing properties:- method can access access and modify obj property using self parameter.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_info(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
p1 = Person("jack", 25)
print(p1.get_info())


# Method modifying properties    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def birthday(self):
        self.age += 1
        return f"My name is {self.name} and I am {self.age} years old."
    
p1 = Person("jack", 25)
print(p1.birthday())
print(p1.birthday())





# The __str__() method is a special method that controls what is returned when the object is printed
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1) # output: Tobias (36)






# without __str__() method, the output will be the object reference
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1) # output: <__main__.Person object at 0x7f8b8c8c8c10> (the memory address will vary)






# Delete Methods
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("Emil")

del Person.greet

p1.greet() # This will cause an error