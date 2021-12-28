#!/usr/bin/env python
# coding: utf-8

# ## Today's agenda: 
# ### OOP PART 1
 
# 1.  Introduction to Object Oriented Programming
# 2.  Python Class
# 3.  Inheritance
# 4.  Polymorphism
# 5.  Encapsulation
# 6.  Abstraction
# 7.  Types of class methods

# ### INTRODUCTION TO OBJECT ORIENTED PROGRAMMING (OOP)
 
# **Procedural Programming**: this is what we've been learning and using so far. It is a way of programming in which we use the code in a step-wise procedure to develop applications. We usually divide the program into small parts, called *procedures*, which are also known as *routines* or *functions* (not to be confused with **functional programming**). 
 
# In other words, **procedural programming** is when we write down a list of instructions to tell the computer what it should do step-by-step to finish a task. 
 
# **Object Oriented Programming**: also a programming approach which recognizes everything as a collection of objects, which all work together to solve a certain problem. It uses self-contained code (i.e. code that is completely independent and contains everything necessary within itself) and is built on the concept of objects that interact with the real world. 
 
# In other words, **OOP** builds programs based on *classes* and a collection of interacting *objects*, which can receive and send messages, and process data.
 
# - OOP is a programming concept that provides patterns for structuring programs where properties and behaviors are bundled into individual objects;
# - Advantages of OOP: development is faster and cheaper, better software maintainability, which results in higher-quality software. However, the learning curve is steeper;
# - Examples of OOP programming languages:  C, C++, Java, Go, Ruby and Python;
# - OOP uses the concept of objects and classes; 
# - A class is a 'blueprint' for objects;
# - OOP is an approach for modeling concrete, real-world things, like ATM machine, a car, as well as relations between things, like companies and employees, students and teachers, and so on;
 
# **Questions about OOP**:
 
# 1. Is it important? -> YES! It is one of the most powerful tools of Python, but very efficient programs can be written without it. 
 
# 2. Is it hard? -> It is different :) Even programmers with a lot of experience in a language that does not use OOP will struggle a bit to understand it. 

# ## OBJECTS
 
# *"Everything in Python is an object"* 
 
# In Python pretty much all the data are objects. Each of the following is an object:
 
# ```
# 123    7.4356    "Hello, world!"    [1, 2, 3, 4]     {"UK": "United Kingdom", "RO": "Romania"}
# 
# Even functions are objects in Python. This might be less obvious, but 
# EVERYTHING THAT CAN BE ASSIGNED TO A VARIABLE IS AN OBJECT IN PYTHON. 
# ```
 
# Each object will have 
# - a type 
# - a data representation (an identity- don't worry about this)
# - a set of procedures for interaction with the object
 
# An object is an *instace* of a *type*:
 
# 1. e.g. ```123``` is an instance of an integer
# 2. e.g. ```[1, 2, 3, 4]``` is an instance of a list
# 3. e.g. ```"Hello, world!"``` is an instance of a string 
 
# In Python we can **create new objects**, **manipulate existing objects**, **delete existing objects**. The beautiful thing is that we don't actually know how these objects are internally represented and you don't need to (OOP and data abstraction). You can find that out, but the only person responsible to know their internal representation is the person that actually created them (e.g. whoever invented the lists or dictionaries). 
 
# We have avoided the term object as much as we could, but we used objects throughout the Foundation. 
 

# ## IMPLEMENTING OUR OWN DATA TYPE
# **How do we implement our own data type? -> with something called CLASSES
# 
# **CLASS**: this is a code template for creating objects. For example, a *dict* or a *list* is a class. 
# - an example of a class is a general class *Cat*;
# - Don't think of it as a specific cat, or your own cat; 
# - We're describing what a cat is and can do, in general;
# - Cats usually have a ```name``` and ```age``` and ```colour```. These are **instance attributes**; 
# - Cats can also ```meow```. This is a **method**;
# 
# - When we talk about a specific cat, you would have an object in programming.
# - An object is an instantiation of a class. 
# - This is the basic principle on which object-oriented programming is based. 
# - *Our example*: this cat belongs to the class *Cat*. His attributes are name = 'Jake' and age = '5'. 
# - A different cat will have different attributes.
# 

# ![Car_OOP](Car_OOP.png)

# ## Complex Class Example

# ![Vehicle_OOP](Vehicle_OOP.png)

# A class defines the blueprint, which can be instantiated to create Object(s)
 
# A class is a code template for creating objects.
 
# Objects have member variables and have behaviour associated with them. In Python a class is created by the keyword class.
 

# ![Flowchart_OOP](Flowchart_OOP.png)

# ### Fun RECAP ### 

# **CLASS**: a structure for defining a type of object. E.g. dictionary, list, string, etc...
 
# **METHODS**: functions associated to a certain class (this should not be new). E.g. .append(), .extend(), etc...
#     > There are 3 types of methods available (I think we will cover these later):
#         >> instance methods;
#         >> class methods (```@classmethod``` decorator);
#         >> static methods (```@staticmethod``` decorator);
# 
# **Instance**: a particular object of a class. E.g. ```[1, 2, 3, 4]``` is an instance of the class List. You can use the type() function to check the class of any object. 
 
# **Attributes**: you can have *class attributes* and *instance attributes* but more on this later. This is simply just assigning and naming variables and allocating them to a certain class or instance. 

# ### EXERCISE 1  --> CREATE & INSTANTIATE A CLASS

# Let's code!


# HOW TO CREATE A CLASS
class Cat:                  #classes are created using the keyword class
    def __init__(self):     #__init__ is a constructor; functions within a class start with self (more on this later)
        pass                # here we will add later the instance variables 

# create an object
jake = Cat()
print(jake)


# ADD ATTRIBUTES TO A CLASS
# perhaps more clear now why the classes are like blueprints
class Cat:                          
    def __init__(self, name, age, breed = None):
        self.name = name            # instance variable
        self.age = age              # instance variable
        self.breed = breed          # instance variable

# create new objects
# this will create an object called jake of the class Cat with the name "Jake", age "5", and breed "Persian"
jake = Cat('Jake', 5) #We call a class by calling the class name and adding in the paranthesis the instances
print(jake.name)
print(jake.age)

print(jake.name + " is " + str(jake.age) + " years old.")


# ## Let's practice 
 
# 1. Using the Cat class, how can we create the following:
#     - Amelia is 10 years old 
#     - John is 2 years old
 
# 2. Using the Cat class, how can we get the following:
#     - Jake is 5 years old and is Persian
 
# Add your answers to the Zoom chat!

# ## EXERCISE

# Write a Python program to create a Vehicle class with colour and max_speed instance attributes.
# 
# Create an instance of the class and print the following: "My car is red and has a maximum speed of 240."

'''ADD YOUR CODE HERE'''


# ## Quiz
 
# What is the difference between a method and a function in Python?

# DEFINE METHODS IN CLASS
class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):             # instance method
        print('Mrr meow meow!')

    def get_info(self):         # instance method
        print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")

# create new objects
# this will create an object called jake of the class Cat with the name "Jake", age "5", and breed "Persian"
jake = Cat('Jake', 5, 'Persian')
# print the method within the class (this is the equivalent of calling the .append() method on a list)
jake.meow()

# create more new objects
# this will create an object called pippa of the class Cat with the name "Pippa", age "3", and breed "Bengal"
pippa = Cat('Pippa', 3, 'Bengal')
# this will create an object called snowy of the class Cat with the name "Snowy", age "8", and breed "Siamese"
snowy = Cat('Snowy', 8, 'Siamese')
# this will create an object called sparky of the class Cat with the name "Sparky", age "2", and breed "Ragdoll"
sparky = Cat('Sparky', 2, 'Ragdoll')

# Now we are trying to print the instance variables of each object by simply calling the new defined method that already has all this information
pippa.get_info()
snowy.get_info()
sparky.get_info()


# *What is 'self'*: 
# - it is a keyword argument that we don't always need to give when calling a method;
# - all instance methods must have this self keyword as the first argument 
# - within a method, self refers to the instance calling the method. When we call the *get_info()* method, we called it through its instance (in the form of ```instance.method()```). The instance is given as the self argument. We could instead do the ```class.method(instance)```


pippa.get_info()
Cat.get_info(pippa) # this is NOT common practice


# ASSIGN NEW VALUE TO THE ATTRIBUTE IN CLASS
class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Mrr meow meow!')

    def get_info(self):
        print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")

    def birthday(self):
        # EXERCISE: add 1 year to the cat's age
        # --- your code goes here ---

# create a new object
jake = Cat('Jake', 5, 'Persian')
print(jake.age)

# call age method
jake.birthday()
print(jake.age)

# PASSING ARGUMENTS TO METHODS
class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print('Mrr meow meow!')

    def get_info(self):
        print(self.name + " is " + str(self.age) + " years old " + self.breed + " cat.")

    def birthday(self):
        self.age += 1

    def set_friend(self, friend):
        # link a friend to this cat and the cat to a friend
        self.friend = friend
        friend.friend = self


# create new objects
snowy = Cat('Snowy', 8, 'Siamese')
sparky = Cat('Sparky', 2, 'Ragdoll')

# Assign Sparky as a friend of Snowy
snowy.set_friend(sparky)

# Let's check snowy's friend settings
print("Print Snowy's friend:", snowy.friend.name)
print("Print Snowy's friend age:", snowy.friend.age)

# same can be done for sparky
print("Print Sparky's friend name:", sparky.friend.name)
print("Print Sparky's friend age:", sparky.friend.age)

# ## THE 4 PRINCIPLES OF OOP 

# ## INHERITANCE
 
# -Inheritance is the process by which one class takes on the attributes and methods of another. 
# - Newly formed classes are called **child classes**
# - The classes that child classes are derived from are called **parent classes**. 
# - Child classes can ```override or extend``` the attributes and methods of parent classes.
# - Child classes ```inherit``` all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.
 

# ![Inheritance_OOP](Inheritance_OOP.png)

# ### EXERCISE 2  --> INHERIT FROM A CLASS


# Create Class Vehicle
class Vehicle:
    def vehicle_method(self):
        print("This is parent Vehicle class method")

# Create Class Car that inherits Vehicle
class Car(Vehicle):
    def car_method(self):
        print("This is child Car class method")

# we create the instance using the child class Car!!!
car_a = Car()

# because Car is a child of Vehicle, we can use all methods from the parent class
car_a.vehicle_method()
# and all methods from the child class 
car_a.car_method()


# ## QUIZ
# What do you think happens in this case?


car_b = Vehicle()
car_b.vehicle_method()
car_b.car_method()



# MULTIPLE CHILDREN OF ONE PARENT CLASS
# let's add another class
class Cycle(Vehicle):
    def cycleMethod(self):
        print("This is child Cycle class method")

car_c = Cycle()
car_c.vehicle_method()



# MULTIPLE PARENTS
class Camera:
    def camera_method(self):
        print("This is parent Camera class method")

class Radio:
    def radio_method(self):
        print("This is parent Radio class method")

# How can we inherit from multiple parents? 
# -- FIX THE CODE BELOW -- 
class MobilePhone():
    def cell_phone_method(self):
        print("This is child MobilePhone class method")

cell_phone_a = MobilePhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()


# **Types of Inheritance** 
# 
# ![Types_Inheritance_OOP](Types_Inheritance_OOP.png)

# ## EXERCISE 
# 
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class:

# Hint: you can use super() which is a temporary object of the superclass and allows us to access methods from it. 
# In our case, we will have to use the super() on the method seating_capacity()


#Example using super(): 
class Animal(object):
  def __init__(self, animal_type):
    print('Animal Type:', animal_type)
    
class Mammal(Animal):
  def __init__(self):

    # call superclass
    super().__init__('Mammal')
    print('Mammals give birth directly')
    
dog = Mammal()

# Output: Animal Type: Mammal
#         Mammals give birth directly


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

'''ADD YOUR CODE HERE'''


# ## POLYMORPHISM
# ### POLY-MORPHISM (MULTIPLE-FORMS)
 
# - Polymorphism is the condition of occurrence in different forms.
# - In programming. It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
 
# **EXAMPLE:**  ```len()``` function is compatible to run with multiple data types
# * ```print(len("CodeFirstGirls"))```
# * ```print(len(["Python", "API", "SQL"]))```
# * ```print(len({"Name": "George", "Age": 10}))```
 
# - The child classes in Python inherit methods and attributes from the parent class. 
# - We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.
# - Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

# - In OOP polymorphism refers to the ability of an object to behave in multiple ways. 
# - It is implemented via method-overloading and method overriding.



'''
METHOD OVERRIDING - a method with the same name in the child class as in the parent class.
The definition of the method differs in parent and child classes but the name remains the same.
'''

class Vehicle:
    def print_details(self):
        print("This is parent Vehicle class method")

class Car(Vehicle):
    def print_details(self):
        print("This is child Car class method")

class Cycle(Vehicle):
    def print_details(self):
        print("This is child Cycle class method")

car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()


# ## EXERCISE
# 
# Create a new class called Dog that overwrites the 2 methods of the below class Cat to match the animal. Create an instance for each class. 

# In[32]:


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


# ### ANSWER

'''ADD YOUR CODE HERE '''


'''
METHOD OVERLOADING - the property of a method to behave in different ways, depending upon the number or types of the parameters.

Example: the same operator can behave in different ways depending on the data type. For example, the + operator adds two numbers, merges two lists, and concatenates two strings. 
1 + 2 -> Output: 3
"Hello" + "World" -> "HelloWorld"
'''
class Car:
   def start(self, a, b=None, c=None):
        if b != None and c != None:
            print(a + b + c)        
        elif b is not None:
            print(a + b)
        else:
            print(a)

car_n = Car()
car_n.start(2)         # in this case a is 2 and b is None 
car_n.start(2, 3)      # in this case a is 2 and b is 3 
car_n.start(2, 3, 4)   # in this case a is 2 and b is 3  and c is 4


# METHOD OVERLOADING as known in other programming languages such as Java, does not really exist in Python. Method Overloading refers to the ability to give multiple
# functions the same name. Example:
# ```
# def our_function(arg_1, arg_2)
# 
# def our_function(arg_1, arg_2, arg_3)
# ```
