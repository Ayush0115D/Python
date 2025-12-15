# Problem 9: Class Inheritance and isinstance()

class Car:
    def __init__(self, brand):
        self.brand = brand


class ElectricCar(Car):
    def __init__(self, brand, battery_size):
        super().__init__(brand)
        self.battery_size = battery_size


# Creating object
my_tesla = ElectricCar("Tesla", "85kWh")

# Using isinstance()
print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True
print(isinstance(my_tesla, int))          # False
 # Multiple Inheritance

class Battery:
    def battery_info(self):
        return "This car has a battery."


class Engine:
    def engine_info(self):
        return "This car has an electric engine."


# ElectricCar inherits from BOTH Battery and Engine
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, battery_size):
        Car.__init__(self, brand)
        self.battery_size = battery_size


# Creating object with multiple inheritance
my_tesla = ElectricCar("Tesla", "85kWh")

# Using methods from both parent classes
print(my_tesla.battery_info())
print(my_tesla.engine_info())