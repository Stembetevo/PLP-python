""" Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" , while Plane.move() prints "Flying" ). """

class Vehicle:
    class Boat:
        def move(self):
            return "Floats" 
    class Car:
        def move(self):
            return "Driving!"

    for vehicle in [Boat(),Car()]:
        print(vehicle.move())
   