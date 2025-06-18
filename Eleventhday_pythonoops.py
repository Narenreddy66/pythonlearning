# Python OOPS
# A class is a blueprint or a template for creating objects while an object is an instance or a copy of the class with actual values.

# Creating a Class:
# Create a class using the class keyword.
class deatils:
    name="Naren"
    age=20
#  creating the objects
obj1=deatils()
print(obj1.name)   

class Details:
    name = "Simran"
    age = 20
 
obj1 = Details()
print(obj1.name)
print(obj1.age)


# self
class Details:
    name="suraj"
    age=24
    def des(self):
        print(f"mu namr is {self.name}and my age is{self.age}")
obj1=Details
obj1.des

# __init__ method
# The __init__ method is used to initialize the object’s state and contains statements that are executed at the time of object creation.
class Details1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj2=Details1("Naren",25) 
# obj2.name="suraj"     
print(f"my name is {obj2.name},age is{obj2.age}")  
        