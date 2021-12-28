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

class Car_2:
    def __init__(self, model):
        self.__model = model

    def get_model(self):
        return self.__model    

my_car = Car_2(2033)
#my_car.__model()
#my_car.get_model()        

my_car.__model = 1092
print(my_car.__model)
print('This is my new model...or is it?', my_car.get_model())


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

# class Car:    
#     def __init__(self, maxspeed, name):
#         self.__maxspeed = maxspeed
#         self.__name = name
    
#     def drive(self):
#         print('driving.maxspeed ' + str(self.__maxspeed))

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

shape1 = Triangle(1, 2, 3)
shape1.calc_perimeter()


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

    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim        

shape = Triangle1(2, 3, 4)
shape.calc_perimeter()

# QUIZ: what do you think happens in the example below? 
showing_instance = Shape1()
print(showing_instance)

# QUIZ: what do you think happens if we don't implement the calc_perimeter method and try the example below?
shape = Triangle1(2, 3, 4)
shape.calc_perimeter()


# ## CLASS METHODS

# To understand class methods, let's first look at the difference between **instance attributes** and **class attributes**.
# 
# - An instance attribute is a Python variable belonging to one, and only one, object. This variable is only accessible in the scope of this object and it is defined INSIDE the constructor function, ```__init__(self,..)``` of the class.
# 
# - A class attribute is a Python variable that belongs to a class rather than a particular object. It is shared between all the objects of this class and it is defined OUTSIDE the constructor function, ```__init__(self,...)```, of the class.

class Bird:
    species = 'bird'    # class attribute

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute


# In[66]:


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

class AnotherCar:
    number_tires = 4
    
    def __init__(self, brand, color, age):
        self.brand = brand
        self.color = color
        self.age = age
        self.number_seats = None   # this is a way of still mentioning an attribute whose value we don't know yet

    @classmethod                                            #class method modifying the class state
    def update_number_of_tires_for_all_cars(cls, tires):
        cls.number_tires = tires

audi = AnotherCar("Audi", "red", 10)
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

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def check_age(age):
        return age > 18

person1 = Person('Jenny', 20)
person2 = Person.details('Fatima', 1992)

print(person1.name, person1.age)
print(person2.name, person2.age)

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

