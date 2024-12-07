""" Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation. """

class Home:
    def __init__(self,color,doors,rooms):
        self.color = color
        self.doors = doors
        self.rooms = rooms 
    

class House(Home):
    pass

home2 = House("Blue","7","6")
home1 = Home("green","4","2")


print(home2.color)
print(home1.color)
