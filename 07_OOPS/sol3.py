# Polymorphism example

class Car:
    def start(self):
        print("Car is starting...")

class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently...")

class DieselCar(Car):
    def start(self):
        print("Diesel car is starting with noise...")

# Polymorphism in action
cars = [
    Car(),
    ElectricCar(),
    DieselCar()
]

for car in cars:
    car.start()   # same method, different behavior
 

# Class variable example
class Vehicle:
    total_vehicles = 0

    def __init__(self, brand):
        self.brand = brand
        Vehicle.total_vehicles += 1

# Creating objects
v1 = Vehicle("Toyota")
v2 = Vehicle("Honda")
v3 = Vehicle("Tata")

# Accessing class variable using class name
print("Total vehicles created:", Vehicle.total_vehicles)