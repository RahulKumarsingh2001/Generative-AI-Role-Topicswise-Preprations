# OOP (object oriented program)
# It is a programming approach in which we organize code using classes and objects.



# Class and Object
# Class: A blueprint for creating objects.
# Object: An instance of a class.

class Student:
    def study(self):
        print("Student is studying")
s1 = Student()
s1.study() # Student is studying

# Student is the class.
# s1 is an object of the Student class.
# study() is a method.
# self refers to the current object.






# __init__() constructor:- __init__() method initializes an object's attributes when an object is created.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 21)
print(s1.name)
print(s1.age)



# oops have 4 pillars:- Encapsulation, Inheritance, Polymorphism, Abstraction


# Encapsulation:- Combining data and methods in a class and controlling access to the data.
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
account = BankAccount(50000)
print(account.get_balance())


# Inheritance:- One class can reuse or extend the functionality of another class.
class Animal:
    def eat(self):
        print("eating...")
class Dog(Animal):
    def bark(self):
        print("bhow bhow..")
        
dog = Dog()
dog.eat()
dog.bark()


# Polymorphism:- Different objects can provide different implementations of the same method.
class Dog:
    def sound(self):
        print("\nbhow bhow1...")
        
class Cat:
    def sound(self):
        print("Meow Meow1...")

for animal in [Dog(), Cat()]:
    animal.sound()     
    

# Abstraction:- Hiding implementation details and exposing only the essential interface.


from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

payment = UpiPayment()
payment.pay(500)
# The abstract class defines what a payment implementation must provide.







# Concept	                    Meaning
# Instance variable	            Data belonging to an individual object
# Class variable	            Data shared at the class level
# Instance method	            Method that receives self
# Class method	                Method that receives cls; uses @classmethod
# Static method	                Utility method inside a class; uses @staticmethod
# Method overriding	            Child class provides its own implementation of a parent method
# Composition	                A class contains or uses objects of another class
# super()	                    Accesses methods from the parent class according to Python's method resolution order                             




# class and instance variables
class Employee:
    company = "Google"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

e1 = Employee("Amit")
e2 = Employee("Priya")
print(e1.name)       # Amit
print(e2.name)       # Priya
print(e1.company)    # Google