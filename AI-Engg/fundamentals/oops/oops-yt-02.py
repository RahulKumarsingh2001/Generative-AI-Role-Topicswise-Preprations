'''
del keyword

Used to delete the object properties or the object itself.

del s1.fullname
del s1
'''

class Student:
    def __init__(self, fullname):
        self.fullname = fullname    

s1 = Student("John Doe")
print(s1.fullname)         # John Doe
del s1.fullname
print(s1.fullname)         # NameError: name 's1' is not defined

        
        
'''
Private Methods and Attributes 

private attribute and method are ment to be used only inside the class and not accessible from outside the class.
'''

class Person:
    __name = "Anonomous"
    
    def __hide_methode(self):
        print("This is a private method ", self.__name)
        
    def welcome(self):
        self.__hide_methode()    


p1 = Person()
print(p1.welcome())






class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # private attrbute (now it is not accessible from outside the class)
        
    def get_acc_pass(self): 
        print(self.__acc_pass)  # we create a public method to access your private attribute


acc1 = Account(123456789, "pass123")
print(acc1.acc_no)  # 123456789
print(acc1.__acc_pass)  # AttributeError: 'Account' object has no attribute
print(acc1.get_acc_pass())  # pass123       
        
        
       
        

      
'''
Inheritance

    Inheritance is a way of creating a new class from an existing class. The new class is called child class
    and the existing class is called parent class.

    class Car:
        pass
    
    class Toyota(Car):
        pass    


There are 3 types of inheritance in Python:
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance

'''
       

# Single Inheritance
class Car:
    color = "Black"     
    @staticmethod
    def start():
        print("Car is started....")
    @staticmethod
    def stop():
        print("Car is stopped....")
        
class Toyota(Car):
    def __init__(self, name):
        self.name = name 
        
        
car1 = Toyota("Toyota Camry")
car2 = Toyota("Toyota Corolla")

print(car1.name)  # Toyota Camry
print(car1.color)  # Black
car2.start()  # Car is started....    





# Multilevel Inheritance                           
class Car:
    color = "Black"     
    @staticmethod
    def start():
        print("Car is started....")
    @staticmethod
    def stop():
        print("Car is stopped....")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand 
        

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type        
        
        
car1 = Fortuner("Diesel")
car1.start()  # Car is started....     




# Multiple Inheritance

class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A, B):
    varC = "Welcome to Class C"
    
c1 = C()

print(c1.varA)  # Welcome to Class A
print(c1.varB)  # Welcome to Class B
print(c1.varC)  # Welcome to Class C




'''
super() method
    -> super method is used to access method of the parent class
'''

class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car is started....")    

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # calling the parent class constructor using super() method
        super().start()  # calling the parent class method using super() method

car1 = ToyotaCar("Fortuner", "Diesel")
print(car1.name)  # Fortuner
print(car1.type)  # Diesel                       





'''
Class Methods
    -> Class methods are used to access class attributes and methods.
    -> Class methods are defined using @classmethod decorator.
    -> Class methods take cls as first parameter which refers to the class itself.

'''


class Person:
    name = "anonymous"
    
    def changeName(self, name):
        Person.name = name  # changing the class attribute using instance method

p1 = Person()
p1.changeName("John Doe")
print(p1.name)  # John Doe
print(Person.name)  # John Doe
        
        
        
class Person:
    name = "anonymous"
    
    def changeName(self, name):
        Person.__class__.name = name  # changing the class attribute using instance method
p1.changeName("John Doe")
print(p1.name)  # John Doe
print(Person.name)  # John Doe
                
                
                
class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls, name):  # cls is a reference to the class itself
        cls.name = name  # changing the class attribute using class method

p1 = Person()
p1.changeName("John Doe")
print(p1.name)  # John Doe
print(Person.name)  # John Doe                        



'''
Now we can learn 3 types of methods in python
1. Instance Method
2. Class Method (cls)
3. Static Method (self)
'''





'''
@property decorator
    we can user @property decorator on any method in the class to use the method as a property.
'''

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((phy + chem + math) / 3) + "%"
        
    def calculate_percentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"    
        
std1 = Student(80, 90, 70)
print(std1.percentage)  # 80.0%


std1.phy = 90
std1.calculate_percentage()
print(std1.percentage)  # 83.33333333333333%



        
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
     
    @property
    def calculate_percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%" 
    
    

std1 = Student(80, 90, 70)   
std1.phy = 90
print(std1.calculate_percentage)  # 83.33333333333333%






'''
Polymorphism: Overloading
    -> Polymorphism means many forms.

different datatypes different meaning are come this is called Operator Overloading also called Polymorphism.   

print(5 + 10)  # 15
print("Hello " + "World")  # Hello World
print([1, 2, 3] + [4, 5, 6])  # merge

 
'''

