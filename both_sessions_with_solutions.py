#!/usr/bin/env python
# coding: utf-8

# ## Today's agenda: 
# ### OOP PART 1
# 
# 1.  Introduction to Object Oriented Programming
# 2.  Python Class </br>
#     **BREAK**
# 3.  Inheritance
# 4.  Polymorphism </br>
#     **BREAK**
# 5.  Encapsulation
# 6.  Abstraction
# 7.  Types of class methods

# ### INTRODUCTION TO OBJECT ORIENTED PROGRAMMING (OOP)
# 
# **Procedural Programming**: this is what we've been learning and using so far. It is a way of programming in which we use the code in a step-wise procedure to develop applications. We usually divide the program into small parts, called *procedures*, which are also known as *routines* or *functions* (not to be confused with **functional programming**). 
# 
# In other words, **procedural programming** is when we write down a list of instructions to tell the computer what it should do step-by-step to finish a task. 
# 
# **Object Oriented Programming**: also a programming approach which recognizes everything as a collection of objects, which all work together to solve a certain problem. It uses self-contained code (i.e. code that is completely independent and contains everything necessary within itself) and is built on the concept of objects that interact with the real world. 
# 
# In other words, **OOP** builds programs based on *classes* and a collection of interacting *objects*, which can receive and send messages, and process data.
# 
# - OOP is a programming concept that provides patterns for structuring programs where properties and behaviors are bundled into individual objects;
# - Advantages of OOP: development is faster and cheaper, better software maintainability, which results in higher-quality software. However, the learning curve is steeper;
# - Examples of OOP programming languages:  C, C++, Java, Go, Ruby and Python;
# - OOP uses the concept of objects and classes; 
# - A class is a 'blueprint' for objects;
# - OOP is an approach for modeling concrete, real-world things, like ATM machine, a car, as well as relations between things, like companies and employees, students and teachers, and so on;
# 
# **Questions about OOP**:
# 
# 1. Is it important? -> YES! It is one of the most powerful tools of Python, but very efficient programs can be written without it. 
# 
# 2. Is it hard? -> It is different :) Even programmers with a lot of experience in a language that does not use OOP will struggle a bit to understand it. 

# ## OBJECTS
# 
# *"Everything in Python is an object"* 
# 
# In Python pretty much all the data are objects. Each of the following is an object:
# 
# ```
# 123    7.4356    "Hello, world!"    [1, 2, 3, 4]     {"UK": "United Kingdom", "RO": "Romania"}
# 
# Even functions are objects in Python. This might be less obvious, but 
# EVERYTHING THAT CAN BE ASSIGNED TO A VARIABLE IS AN OBJECT IN PYTHON. 
# ```
# 
# Each object will have 
# - a type 
# - a data representation (an identity- don't worry about this)
# - a set of procedures for interaction with the object
# 
# An object is an *instace* of a *type*:
# 
# 1. e.g. ```123``` is an instance of an integer
# 2. e.g. ```[1, 2, 3, 4]``` is an instance of a list
# 3. e.g. ```"Hello, world!"``` is an instance of a string 
# 
# In Python we can **create new objects**, **manipulate existing objects**, **delete existing objects**. The beautiful thing is that we don't actually know how these objects are internally represented and you don't need to (OOP and data abstraction). You can find that out, but the only person responsible to know their internal representation is the person that actually created them (e.g. whoever invented the lists or dictionaries). 
# 
# We have avoided the term object as much as we could, but we used objects throughout the Foundation. 
# 

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
# 
# A class is a code template for creating objects.
# 
# Objects have member variables and have behaviour associated with them. In Python a class is created by the keyword class.
# 

# ![Flowchart_OOP](Flowchart_OOP.png)

# ### EXERCISE 1  --> CREATE & INSTANTIATE A CLASS
# 
# Let's code!

# In[1]:


# HOW TO CREATE A CLASS
class Cat:                  #classes are created using the keyword class
    def __init__(self):     #__init__ is a constructor; functions within a class start with self (more on this later)
        pass                # here we will add later the instance variables 

# create an object
jake = Cat()
print(jake)


# In[6]:


# ADD ATTRIBUTES TO A CLASS
# perhaps more clear now why the classes are like blueprints
class Cat:                          
    def __init__(self, name, age, breed = None):
        self.name = name            # instance variable
        self.age = age              # instance variable
        self.breed = breed          # instance variable

# create new objects
# this will create an object called jake of the class Cat with the name "Jake", age "5"
jake = Cat('Jake', 5, 'Persian') #We call a class by calling the class name and adding in the paranthesis the instances
print(jake.name)
print(jake.age)

print(jake.name + " is " + str(jake.age) + " years old.")

amelia = Cat('Amelia',10)
john = Cat('John',2)


# ## Let's practice 
# 
# 1. Using the Cat class, how can we create the following:
#     - Amelia is 10 years old 
#     - John is 2 years old
# 
# 2. Using the Cat class, how can we get the following:
#     - Jake is 5 years old and is Persian
# 
# Add your answers to the Zoom chat!

# ## EXERCISE

# Write a Python program to create a Vehicle class with colour and max_speed instance attributes.
# 
# Create an instance of the class and print the following: "My car is red and has a maximum speed of 240."

# In[12]:


class Vehicle:
    def __init__(self, colour, max_speed):
        self.colour = colour
        self.max_speed = max_speed

modelX = Vehicle('red', 240)
print(f'My car is {modelX.colour} and has a maximum speed of {modelX.max_speed}')


# ## Quiz
# 
# What is the difference between a method and a function in Python?

# In[7]:


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

# In[ ]:


jake.get_info()
Cat.get_info(pippa) # this is NOT common practice


# In[13]:


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
        self.age += 1  

# create a new object
jake = Cat('Jake', 5, 'Persian')
print(jake.age)

print(jake.get_info())

# call age method
jake.birthday()
print(jake.age)


# In[ ]:


# ANSWER: 
# def birthday(self):
#     # EXERCISE: add 1 year to the cat's age
#     # --- your code goes here ---
#     self.age += 1    


# In[14]:


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


# In[15]:


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


# ### Fun RECAP ### 
# 
# **CLASS**: a structure for defining a type of object. E.g. dictionary, list, string, etc...
# 
# **METHODS**: functions associated to a certain class (this should not be new). E.g. .append(), .extend(), etc...
#     
#     > There are 3 types of methods available (class and static later):
#         >> instance methods;
#         >> class methods (@classmethod decorator);
#         >> static methods (@staticmethod decorator);
# 
# **Instance**: a particular object of a class. E.g. ```[1, 2, 3, 4]``` is an instance of the class List. You can use the type() function to check the class of any object. 
# 
# **Attributes**: you can have *class attributes* and *instance attributes* but more on this later. This is simply just assigning and naming variables and allocating them to a certain class or instance. 

# ## <center> 5 MINUTE BREAK </center>

# ## THE 4 PRINCIPLES OF OOP 

# ## INHERITANCE
# 
# -Inheritance is the process by which one class takes on the attributes and methods of another. 
# - Newly formed classes are called **child classes**
# - The classes that child classes are derived from are called **parent classes**. 
# - Child classes can ```override or extend``` the attributes and methods of parent classes.
# - Child classes ```inherit``` all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.
# 

# ![Inheritance_OOP](Inheritance_OOP.png)

# ### EXERCISE 2  --> INHERIT FROM A CLASS

# In[18]:


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

# and all methods from the child class 
car_a.car_method()
# because Car is a child of Vehicle, we can use all methods from the parent class
car_a.vehicle_method()


# ## QUIZ
# What do you think happens in this case?

# In[19]:


car_b = Vehicle()
car_b.vehicle_method()
car_b.car_method()


# In[ ]:


# MULTIPLE CHILDREN OF ONE PARENT CLASS
# let's add another class
class Cycle(Vehicle):
    def cycleMethod(self):
        print("This is child Cycle class method")

car_c = Cycle()
car_c.vehicle_method()


# In[20]:


# MULTIPLE PARENTS
class Camera:
    def camera_method(self):
        print("This is parent Camera class method")

class Radio:
    def radio_method(self):
        print("This is parent Radio class method")

# How can we inherit from multiple parents? 
# -- FIX THE CODE BELOW -- 
class MobilePhone(Camera, Radio):
    def cell_phone_method(self):
        print("This is child MobilePhone class method")

cell_phone_a = MobilePhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()


# In[ ]:


# ANSWER 
# class MobilePhone(Camera, Radio):
#     def cell_phone_method(self):
#         print("This is child MobilePhone class method")


# **Types of Inheritance** 
# 
# ![Types_Inheritance_OOP](Types_Inheritance_OOP.png)

# ## EXERCISE 
# 
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class:

# Hint: you can use super() which is a temporary object of the superclass and allows us to access methods from it. 
# In our case, we will have to use the super() on the method seating_capacity()

# In[ ]:


#Example: 
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


# In[ ]:


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


# ### ANSWER

# In[32]:


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


# In[28]:


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity = 50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


# ## POLYMORPHISM
# ### POLY-MORPHISM (MULTIPLE-FORMS)
# 
# - Polymorphism is the condition of occurrence in different forms.
# - In programming. It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
# 
# **EXAMPLE:**  ```len()``` function is compatible to run with multiple data types
# * ```print(len("CodeFirstGirls"))```
# * ```print(len(["Python", "API", "SQL"]))```
# * ```print(len({"Name": "George", "Age": 10}))```
# 
# - The child classes in Python inherit methods and attributes from the parent class. 
# - We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.
# - Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

# - In OOP polymorphism refers to the ability of an object to behave in multiple ways. 
# - It is implemented via method-overloading and method overriding.

# In[ ]:


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

# In[33]:


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# In[31]:


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

# ## EXERCISES
# 
# ### Exercise 1
# - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
# 
# ### Exercise 2
# - Create a Python class Person with attributes: name and age of type string.
# - Create a display() method that displays the name and age of an object created via the Person class.
# - Create a child class Student  which inherits from the Person class and which also has a section attribute.
# - Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# - Create a student object via an instantiation on the Student class and then test the displayStudent method.

# In[16]:


class String():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = String()
str1.get_String()
str1.print_String()


# In[54]:


class Person:
    # define constructor with name and age as parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create display method fro Person class
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
    
# create child class Student of Person class
class Student(Person):
    # define constructor of Student class with section additional parameters 
    def __init__(self):
        super().__init__(self)
        # OR
        #Person.__init__(self, name, age)
        self.section = section
   
    # Create display method for Student class
    def displayStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)
    
# Testing Person class
P = Person("Tomas Wild", 37)
P.display()
print("-------------------------------")
S = Student("Mathematics")
S.displayStudent()


# ## ENCAPSULATION

# Consider a *real-life example* of encapsulation, in a company, there are **different sections** like the accounts section, finance section, sales section etc. The ```finance section``` handles all the financial transactions and keeps records of all the data related to finance. Similarly, the ```sales section``` handles all the sales-related activities and keeps records of all the sales. 
# 
# Now there may arise a situation when for some reason an ```official from the finance section``` needs ```all the data``` about ```sales``` in a particular month. In this case, he is ```not allowed to directly access the data of the sales section```. He will first have to contact some other officer in the sales section and then request him to give the particular data. This is what encapsulation is. Here the data of the sales section and the employees that can manipulate them are wrapped under a single name “sales section”. Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
# 
# 
# - It refers to data hiding. In OOP one class should not have direct access to the data of the other class.
# - restricting the access to variables or/and methods; 
# - Advantages: it prevents data from being modified by accident
# 
# There are 3 levels of restriction in Python:
# - Public or no restriction: we can access and modify these as we like 
#    > -> created by simply defining the method (what we saw so far). Example: meow
# - Private: accessed only from within its own class or object (they cannot be modified from outside of their class)  
#    > -> it is created with 2 underscores before the name. Example: __meow
# - Protected: can be accessed within the class and the classes derived from that class (not often common and not very good in Python)
#    > -> it is created with 1 underscore before the name. Example: _meow
#  

# In[25]:


class Car_2:
    def __init__(self, model):
        self.__model = model

    def get_model(self):
        return self.__model    

my_car = Car_2(2033)
#my_car.__model
#my_car.get_model()        

my_car.__model = 1092
print(my_car.__model)
print('This is my new model...or is it?', my_car.get_model())


# In[ ]:


# some of the examples used to show Encapsulation are modified from: https://pythonspot.com/encapsulation/

''' Using public instance variables '''

# class Car:    
#     def __init__(self, maxspeed, name):
#         self.maxspeed = maxspeed
#         self.name = name
    
#     def drive(self):
#         print('driving.maxspeed ' + str(self.maxspeed))

# redcar = Car(100, "Supercar")
# redcar.drive()
# redcar.maxspeed = 10  # will change the variable as the variable is public
# redcar.drive()
# print(redcar.maxspeed, redcar.name)

''' Using private instance variables '''

class Car:    
    def __init__(self, maxspeed, name):
        self.__maxspeed = maxspeed
        self.__name = name
    
    def drive(self):
        print('driving.maxspeed ' + str(self.__maxspeed))

# redcar = Car(100, "Supercar")
# redcar.drive()
# redcar.__maxspeed = 10  # will not change variable because its private
# redcar.drive()
# print(redcar.__maxspeed, redcar.__name)


# In ENCAPSULATION, the variables and methods can only be interacted with based on some predefined interfaces designed by the class itself. 
# 
# These are called: 
# - ```getter methods```: used to retrieve values from variables
# - ```setter methods```: used to set values to variables
# 
# In other words, to change the value of a private variable, we use a setter method (this is all this method can do - set the value of a private variable). 

# In[27]:


class Car:    
    def __init__(self, maxspeed, name):
        self.__maxspeed = maxspeed
        self.__name = name
    
    # getter method
    def drive(self):
        print('driving.maxspeed ' + str(self.__maxspeed))

    # setter method
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed

redcar = Car(200, "Supercar")
redcar.drive()
#redcar.__maxspeed = 100
redcar.setMaxSpeed(320)
redcar.drive()


# Python is not extremely good at hiding data. These are just conventions that allow us to indicate that someone should not be modifying those variables or calling the methods from outside the class, but there is no way to strictly enforce this. You can read more about this [here](https://docs.python.org/3/tutorial/classes.html#tut-private) and some other examples [here](https://stackoverflow.com/questions/34808525/python-has-or-not-access-modifiers). 

# ## ABSTRACTION
# 
# - An abstract class can be considered as a blueprint for other classes. 
# - It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
# - A class which contains one or more abstract methods is called an abstract class. 
# - An abstract method is a method that has a declaration but does not have an implementation. 
# - When we want to provide a common interface for different implementations of a component, we use an abstract class.

# ![Abstraction_OOP](Abstraction_OOP.png)

# In[31]:


class Shape:

    def calc_perimeter(self):
        raise NotImplementedError("Please Implement this method")

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def calc_perimeter(self):
    #     perim = self.a + self.b + self.c
    #     print("Consider me implemented", perim)
    #     return perim


# In[33]:


shape1 = Triangle(1, 2, 3)
#shape1.calc_perimeter()


# **HOWEVER** Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods. The above is not an abstract class because:
# - we can instantiate an instace from; run the below code if you don't know what this refers to
# 
# ``` 
# showing_instance = Shape()
# print(showing_instance)
# ```
# 
# - we are not required to implement calc_perimiter in the Triangle class;
# 
# The above example works because it uses the principles of Inheritance and Polymorphism:
# - Triangle inherits all methods of the Shape class;
# - when we define calc_perimeter in the Triangle class, we simply overwrite it;

# In[36]:


from abc import ABC, abstractmethod, ABCMeta # abc stands for Abstract Base Classes
# ABC is "a class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from 
# ABC avoiding sometimes confusing metaclass usage" (Python abc package documentation: https://docs.python.org/3/library/abc.html)

class Shape1(ABC):
    @abstractmethod             # this makes the method abstract (i.e. a method which you must implement in the subclass)
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle1(Shape1):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def calc_perimeter(self):
    #     perim = self.a + self.b + self.c
    #     print("Consider me implemented", perim)
    #     return perim        


# In[37]:


shape = Triangle1(2, 3, 4)
shape.calc_perimeter()


# In[38]:


# QUIZ: what do you think happens in the example below? 
showing_instance = Shape1()
print(showing_instance)


# In[ ]:


# QUIZ: what do you think happens if we don't implement the calc_perimeter method and try the example below?
shape = Triangle1(2, 3, 4)
shape.calc_perimeter()


# ## CLASS METHODS

# To understand class methods, let's first look at the difference between **instance attributes** and **class attributes**.
# 
# - An instance attribute is a Python variable belonging to one, and only one, object. This variable is only accessible in the scope of this object and it is defined INSIDE the constructor function, ```__init__(self,..)``` of the class.
# 
# - A class attribute is a Python variable that belongs to a class rather than a particular object. It is shared between all the objects of this class and it is defined OUTSIDE the constructor function, ```__init__(self,...)```, of the class.

# In[40]:


class Bird:
    species = 'bird'    # class attribute

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute


# In[41]:


bird_1 = Bird('Randy', 10)
bird_2 = Bird('Mandy', 5)

print(f'{bird_1.name} is {bird_1.age} and is a {bird_1.species}')
print(f'{bird_2.name} is {bird_2.age} and is a {bird_2.species}')


# ## QUIZ
# 
# What did we use the **instance methods** (i.e., all the methods we've seen so far) for? What did we access? 
# 
# What do you think we will use **class methods** for? 

# ```@classmethod```
# - Declares a class method;
# - The idea is very similar to the one for *instance methods*; 
# - Instead of using the *self* parameter, it takes a *cls* parameter that points to the class rather than the instance;
# - It can access class attributes, but not the instance attributes;
# - Because it only has access to the *cls* argument, it cannot modify object instance state;
# - It can be called using the ```ClassName.MethodName()``` or ```object.MethodName()```;

# In[45]:


class AnotherCar:
    number_tires = 4
    
    def __init__(self, brand, color, age, number_seats):
        self.brand = brand
        self.color = color
        self.age = age
        self.number_seats = None   # this is a way of still mentioning an attribute whose value we don't know yet

    @classmethod                                            #class method modifying the class state
    def update_number_of_tires_for_all_cars(cls, tires):
        cls.number_tires = tires


# In[46]:


audi = AnotherCar("Audi", "red", 10, 3)
print(audi.number_seats)


# In[43]:


audi = AnotherCar("Audi", "red", 10, 3)
bmw = AnotherCar("BMW", "white", 5)

print(f'Default value for number_tires: - {AnotherCar.number_tires} - and the number_tires for audi: - {audi.number_tires} -')
audi.number_tires = 6
print(f'Default value for number_tires: - {AnotherCar.number_tires} -, number_tires for audi: - {audi.number_tires} and number_tires for bmw: - {bmw.number_tires} -')
AnotherCar.update_number_of_tires_for_all_cars(6)
print(f'Default value for number_tires: - {AnotherCar.number_tires} -, number_tires for audi: - {audi.number_tires} and number_tires for bmw: - {bmw.number_tires} -')


# ```@staticmethod```
# - Declares a static method;
# - It cannot access either class attributes or instance attributes;
# - Takes neither a *self* nor a *cls* argument;
# - It is simply a function defined inside a class that cannot modify object or class states;
# - It can be called using the ```ClassName.MethodName()``` or ```object.MethodName()```;
# - It cannot return an object of the class;
# 
# *Static methods* are utility functions and work on data provided to them in arguments (NOTE: no 'self' passed in). Usually, they are a way to group functions together that have some logical connection with a certain class.
# 
# ```utility function``` = are functions re-used in the program with the aim of reducing the complexity and improve the readibility of the program. Examples might include methods connecting to databases, performing string manipulations, sorting and searching of collections of data, writing/reading data to/from files and so on.

# In[47]:


from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def check_age(age):
        return age > 18

person1 = Person('Jenny', 20)
#person2 = Person.details('Fatima', 1992)

print(person1.name, person1.age)
#print(person2.name, person2.age)

print(Person.check_age(33))


# ## OOP TERMINOLOGY
# 
# - **Class** − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
# - **Class variable** − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
# - **Data member** − A class variable or instance variable that holds data associated with a class and its objects.
# - **Function overloading** − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.
# - **Instance variable** − A variable that is defined inside a method and belongs only to the current instance of a class.
# - **Inheritance** − The transfer of the characteristics of a class to other classes that are derived from it.
# - **Instance** − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
# - **Instantiation** − The creation of an instance of a class.
# - **Method** − A special kind of function that is defined in a class definition.
# - **Object** − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.
# - **Operator overloading** − The assignment of more than one function to a particular operator.

# ## Today's agenda: 
# ### OOP PART 2
# 
# 1.  SOLID Principles in OOP </br>
# - Single Responsibility
# - Open-Closed
# - Liskov Substitution
# - Interface Segregation
# - Dependency Injection 

# ```SOLID``` is a *mnemonic abbreviation* for a set of design principles created for software development in object-oriented languages. 
# 
# The principles in SOLID are intended to foster simpler, more robust and updatable code from software developers. 
# Each letter in SOLID corresponds to a principle for development
# 
# - The Single-Responsibility Principle (SRP)
# - The Open-Closed Principle (OCP)
# - The Liskov Substitution Principle (LSP)
# - The Interface Segregation Principle (ISP)
# - The Dependency Inversion Principle (DIP)
# 
# ```SOLID``` design was created many many years ago as an attempt to avoid the 'spaghetti code'. It comes as a helper to support programmers in avoiding creating code that is RIGID (one change in place X affects many other components), FRAGILE (you change something in place X and then something in place Y, Z, K, alpha, beta, etc break), IMMOBILE (the code you build can only be used in the specific context). 

# Side note: almost all the examples in this script are from [here](https://towardsdatascience.com/5-principles-to-write-solid-code-examples-in-python-9062272e6bdc). The explanations are also very good so if you get stuck, have a look at the article. Also very good explanations [here](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94).

# ### Single Responsibility
# 
# ```A class should have only one job and therefore it should have only a single reason to change.```
# 
# Not to be mistakes with a class having only one function. It can have multiple functions but that work along the same lines. If different parts change for different reasons, then maybe you might want to rethink/refactor your class. 
# 
# To state this principle more technically: Only one potential change (database logic, logging logic, and so on.) in the software’s specification should be able to affect the specification of the class.
# This means that if a class is a data container, like a Book class or a Student class, and it has some fields regarding that entity, it should change only when we change the data model.
# 
# For example, generally speaking a function that does a lot of different things, such as reading data, modifying it, doing some calculations, plotting some results, and then ending, would not be a very good way to write code. Same principle applies here only translated to OOP.

# In[ ]:


class Album:
    # that None is a function annotation (explained here: https://www.python.org/dev/peps/pep-3107/)
    def __init__(self, name, artist, songs) -> None:    # this -> None as is in here does absolutely nothing; it is an annotation
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    # breaks the SRP !!!
    def search_album_by_artist(self):
        """ Searching the database for other albums by same artist """
        pass

# INSTEAD CREATE ANOTHER CLASS

class AlbumBrowser:
    """ Class for browsing the Albums database"""
    def search_album_by_artist(self, albums, artist):
        pass

    def search_album_starting_with_letter(self, albums, letter):
        pass

'''However, this solution, even though it does not break the SRP principle anymore, it breaks the OCP.'''


# ### Open-Closed
# 
# ``` Software entities(Classes, modules, functions) should be open for extension, not modification. ```
# 
# This means that you will want to extend the functionality of a class but without necessarily modifying it. In other words, you should not need to modify the code you have already written to accommodate new functionality, but simply add what you need now.
# 

# In[5]:


# BEFORE
class AlbumBrowser:
    def search_album_by_artist(self, albums, artist):
        return [album for album in albums if album.artist == artist]

    def search_album_by_genre(self, albums, genre):
        return [album for album in albums if album.genre == genre]

    # Now what happens if we want to search by artist or by genre?
    # What if we add release year?
    # We will have to write a new function every time modifying the class!


# INSTEAD
class SearchBy:
    def is_matched(self, album):
        pass

class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre

    def is_matched(self, album):
        return album.genre == self.genre


class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist

    def is_matched(self, album):
        return album.artist == self.artist


class AlbumBrowser:
    # Note we pass one of the classes as searchby arg
    def browse(self, albums, searchby):
        return [album for album in albums if searchby.is_matched(album)]


# ### Liskov-Substitution Priciple
# 
# ```If class A is a subtype of class B, then we should be able to replace B with A without disrupting the behavior of our program.```
# 
# The main idea behind Liskov Subtitution Principle is that, for any class, a client should be able to use any of its subtypes indistinguishably, without even noticing, and therefore without compromising the expected behavior at runtime. 
# This means that clients are completely isolated and unaware of changes in the class hierarchy.
# 

# ![Liskov-Substitution Principle](LiskovSubtitutionPrinciple_Simon.jpg)

# In[ ]:


# we already have this class Album, let's copy it over
class Album:
    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)


# This subclass behave the same way as its parent class.
class BestOfCompilation(Album):
    def __init__(self, name, artist, songs):
        super().__init__(name, artist, songs)


# ### Interface Segregation Principle
# 
# ``` Larger interfaces should be split into smaller ones. By doing so, we can ensure that implementing classes only need to be concerned about the methods that are of interest to them “Clients should not be forced to depend upon interfaces that they do not use.” ```

# In[7]:


class PlaySongs:
    def __init__(self, title):
        self.title = title

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")

    def sing_lyrics(self):
        print("Lalalalala")


# This class is fine, just changing the guitar and lyrics
class PlayRockSongs(PlaySongs):
    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you!")


# This breaks the ISP, we don't have lyrics!!!!!
class PlayInstrumentalSongs(PlaySongs):
    def sing_lyrics(self):
        raise Exception("No lyrics for instrumental songs")


# INSTEAD

from abc import abstractmethod

class PlaySongsLyrics:
    @abstractmethod
    def sing_lyrics(self):
        pass


class PlaySongsMusic:
    @abstractmethod
    def play_guitar(self):
        pass

    @abstractmethod
    def play_drums(self):
        pass


class PlayInstrumentalSong(PlaySongsMusic):
    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")


class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):
    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you")

    def play_drums(self):
        print("Bum-bum-bum")


# ### Dependency Inversion Principle
# 
# ``` Dependency Inversion (injection) refers to the decoupling of software modules. This way, instead of high-level modules depending on low-level modules, both will depend on abstractions. "High-level modules should not depend on low-level modules." ```

# In[8]:


class AlbumShop:
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))


class ViewRockAlbums:
    def __init__(self, album_shop):
        for album in album_shop.albums:
            if album[2] == "Rock":
                print("We have {} in our shop.".format(album[0]))

    # IMPORTANT
    # ViewRockAlbums explicitly depends on the fact that albums are stored in a tuple in a certain order inside AlbumShop.
    # It should have no knowledge of the internal structure of AlbumShop.
    # Now if we change the ordering in the tuples in the album, our code would break.


# INSTEAD

class GeneralAlbumShop:
    @abstractmethod
    def filter_by_genre(self, genre):
        pass


class MyAlbumShop(GeneralAlbumShop):
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))

    def filter_by_genre(self, genre):
        for album in self.albums:
           if album[2] == genre:
                yield album[0]


class ViewRockAlbums:
    def __init__(self, album_store):
        for album_name in album_store.filter_by_genre("Rock"):
            print("We have {} in our shop.".format(album_name))

    # NOTE: if we had another type of AlbumShop, that decides to store the album differently,
    # it would need to implement the same interface for filter_by_genre to make ViewRockAlbums work.

