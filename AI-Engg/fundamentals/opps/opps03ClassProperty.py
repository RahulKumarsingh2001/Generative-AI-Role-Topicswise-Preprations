# Class Property:-  Properties are variables that belong to a class.

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("Jon", 18);
print(p1.name)
print(p1.age)



# Access Property:- you can any property with the dot notation.



# Modify property
p1.age = 24
print(p1.age)



# delete property
del p1.age
# print(p1.age) # ❌ this will raise an error because the age property has been deleted        




# Class Properties vs Object Properties
class Person:
    schoolname = "ABC School" # class property
    def __init__(self, name, age):
        self.name = name # object property
        self.age = age # object property
p1 = Person("Jon", 18)
print(p1.name) # object property
print(p1.age) # object property
print(Person.schoolname) # class property




# Modify Class Properties
Person.schoolname = "XYZ School"
print(Person.schoolname)     



# Add new property
Person.country = "India"
print(Person.country)    
        