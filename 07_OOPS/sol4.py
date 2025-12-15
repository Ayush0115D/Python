# Static Method + Property Decorator (Read-only attribute)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model   # protected attribute (internal use)

    # ---------------- Problem 7 ----------------
    # Static method: does not use self or class data
    @staticmethod
    def general_description():
        return "A car is a vehicle used for transportation."

    # Property decorator to make model read-only
    @property
    def model(self):
        return self._model


# Creating object
my_car = Car("Toyota", "Corolla")

# Using static method
print(Car.general_description())

# Accessing read-only property
print("Car model:", my_car.model)

# ❌ This will cause error because model is read-only
# my_car.model = "Camry"
