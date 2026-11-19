'''
Object-Oriented Programming (OOP) in Python


Classes and Objects

A classes is a blueprint of creating a objects
and also class is a collection of 2 things Methods and Attributes.
'''

# Creating a class 
class Student:
    name = "John"

# Creating objects (instance)
s1 = Student()
print(s1.name)



'''
Constructor in Python

A classes have a function called __init__(),
which is always executesd when the object is being initiated.


# Creating a class                        # Creating objects (instance)       
class Student:                            s1 = Student("John Doe")
    def __init__(self, fullname):         print(s1.fullname)                 
        self.fullname = fullname


self -> it refers to the current instance of the class, and used to access variables that belongs to the class.
'''


    
class Student:
    def __init__(self, fullname):
        self.fullname = fullname     # here self.fullname is a attribute (variable = attribute)
        
s1 = Student("John Doe")
print(s1.fullname)        




'''
generally constructors are two types 
1. Default Constructor
2. Parameterized Constructor
'''

class Student:
    def __init__(self):   # Default Constructor
        pass
    
    def __init__(self, fullname):   # parameterized Constructor
        self.fullname = fullname
        
        




'''
Attributes are 2 types
1. Instance/ Object Attributes
    -> Usually defined inside the constructor using self keyword.
    -> Each Object have different values
    
    
2. Class Attributes
    -> Belong to the class
    -> shared among all the objects of the class
'''

class Student:
    college = "GIET"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

s1 = Student("Rahul")
s2 = Student("Amit")





'''
Methods

Method are a functions that belongs to objects.

There are 3 types of methods
1) Instance Method
    -> it take a self parameter as a first parameter.
    -> Can access and modify instance attributes and class attributes.
    -> Used when we want to work with individual object data.
    
2) Class Method
    -> it take a cls parameter as a first parameter.
    -> Can access and modify class attributes.
    -> Uses the @classmethod decorator.
    
3) Static Method
    -> it doesn't take any specific parameter.
    -> Cannot directly access instance or class attributes.
    -> Uses the @staticmethod decorator.
'''


class Student:

    college = "GIET"

    def instance_method(self):
        print(self.college)

    @classmethod
    def class_method(cls):
        print(cls.college)

    @staticmethod
    def static_method():
        print("Hello Student")
        
        
        
        


# we can create a simple class take a student name and 3 marks and give avg marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks        
    
    def average_marks(self):
        sum = 0
        for val in self.marks:
            sum = sum + val
        print(f"Average marks of {self.name} is {sum/len(self.marks)}")
        

s1 = Student("Rahul", [85, 90, 78])
s1.average_marks()  # Average marks of Rahul is 84.333333333333        
            