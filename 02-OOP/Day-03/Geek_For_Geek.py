#Inheritance in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()

#super() Function
# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Calls constructor based on MRO
        super().__init__(name)  
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info() # Parent method
d.details()   # Child method

#Method Overriding in Inheritance
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()

### Method Overloading in Inheritance
#Method Overloading means defining multiple methods with the same name but different parameter lists (number, type, or order of parameters).

"""
METHOD OVERLOADING IN PYTHON

Same method name with different numbers of arguments.
"""

class Calculator:

    def add(self, *args):

        if len(args) == 2:
            return args[0] + args[1]

        elif len(args) == 3:
            return args[0] + args[1] + args[2]

        else:
            return "Invalid number of arguments"


# ==================== MAIN PROGRAM ====================

calc = Calculator()

# Two arguments
print(calc.add(10, 20))

# Three arguments
print(calc.add(10, 20, 30))
