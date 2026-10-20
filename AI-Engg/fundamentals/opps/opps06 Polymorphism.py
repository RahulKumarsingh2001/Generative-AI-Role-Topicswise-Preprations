# Polymorphism

# Polymorphism means “many forms.” In Python, it allows the same method name, function, 
# or interface to behave differently depending on the object or the data it receives.



# Polymorphism with diff class
class Dog:
    def speak(self):
        print("Woof!")
        
class Cat:
    def speak(self):
        print("Meow!")
        
dog = Dog()
cat = Cat()

dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!







# Polymorphism using a common function
class Dog:
    def speak(self):
        print("Woof!")
        
class Cat:
    def speak(self):
        print("Meow!")

def make_sound(animal):
    print(animal.speak())
    
make_sound(Dog())  # Output: Woof!
make_sound(Cat())  # Output: Meow!    
                         





# Polymorphism through inheritance (method overriding)
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()  # Animal makes a sound
dog.sound()     # Dog barks







# Polymorphism with built-in functions
print(len("Python"))       # 6
print(len([10, 20, 30]))   # 3
print(len({"a": 1, "b": 2}))  # 2