#Object Oriented Programming empowers developers to build modular, 
#maintainable and scalable applications

#Modular
#OOP Modular means dividing a large software application into smaller, independent, reusable components (classes and objects), where each component has its own responsibility.
class Student:
    def register(self):
        print("Student Registered")

class Teacher:
    def take_attendance(self):
        print("Attendance marked")
class Payment:
    def pay_fee(self):
        print("Fee paid")


student = Student()
teacher = Teacher()
payment = Payment()

student.register()
teacher.take_attendance()
payment.pay_fee()

#Maintainable means software that is easy to understand, fix, modify, and update in the future without breaking other parts of the application.
class Student:
    def register(self):
        print("Student registered")


class Teacher:
    def manage_teacher(self):
        print("Teacher managed")


class Payment:
    def pay_fee(self):
        print("Fee paid")

#Scalable Applications
#Scalable Applications means software applications that can handle an increase in users, data, and workload without significantly affecting performance.

#In simple words: Jab application par users ya workload increase ho, to application usay efficiently handle kar sake.
class Student:
    def __init__(self, name):
        self.name = name


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


system = StudentManagement()

system.add_student(Student("Jawad"))
system.add_student(Student("Ali"))

print(len(system.students))

#Class
#A Class is a blueprint or template used to create objects. It defines the attributes (data) and methods (behaviour) that its objects will have.

#In simple words: Class aik blueprint hoti hai, aur object us blueprint se banne wali actual entity hoti hai.
class Car:

    # Constructor
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method
    def start(self):
        print("Car is starting")


# Creating objects
car1 = Car("BMW", "Black")
car2 = Car("Toyota", "White")

print(car1.brand)
print(car2.brand)

car1.start()

# Objects 
""" Objects
An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data. An object consists of:

State: represented by the attributes and reflects the properties of an object.
Behavior: represented by the methods of an object and reflects the response of an object to other objects.
Identity: gives a unique name to an object and enables one object to interact with other objects. """

# Creating Object
print("\n")
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.age)
print(dog1.species)
print("\n")

#Four Pillars of OOP
""" Four Pillars of Object-Oriented Programming (OOP) form the foundation for designing structured, reusable and maintainable software. """
#01 Encapsultaion (Data Security)
""" Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. A class is an example of encapsulation as it groups together member functions, variables and other related data in a single unit. """
class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
# print(emp.__salary)

print("\n")
class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ${self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount             # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()           # Accessing protected method
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._show_balance()      # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally
#-1 Access modifiers (public, private,public)

# 04 Data Abstraction
""" Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it."""
from abc import ABC,abstractmethod
#Abstract class (Data Hiding)
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

#Concrete Class 
class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using Credit Card")
class Jaazcash(ABC):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using Jaazcash ")
# Objects
payment1 = CreditCard()
payment2 = Jaazcash()
payment1.pay(5000)
payment2.pay(2000)

#Inheritance
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

"""
ENCAPSULATION IN PYTHON

Encapsulation explains two things:

1. An object's characteristics (attributes) and
   behaviours (methods) are encapsulated together
   within that object.

2. All characteristics and behaviours should not be
   directly accessible to everyone.

   Objects should provide controlled access to data.

We implement encapsulation by:

1. Creating a class that acts as a blueprint for objects.
   The class contains attributes and methods together.

2. Using access conventions and properties to control
   access to class attributes.

Example:
SportsCar represents a real-world sports car.
"""

