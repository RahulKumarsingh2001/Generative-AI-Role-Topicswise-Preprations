# Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.




class Parents:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("hey, ",self.name)


class Child(Parents):
    pass


x1 = Parents("Emil")
x2 = Child("Tobias")

# print(x1.printName())
print(x2.name)   
x2.printName()    
               
               



# super() function that will make the child class inherit all the methods and properties from its parent
class Person:
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("hey, ",self.name)
        
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.school = "ABC School"
x = Student("ABC")
print(x.name)                                     
print(x.school)                                     