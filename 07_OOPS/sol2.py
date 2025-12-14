# Encapsulation example

class Car:
    def __init__(self, brand, model):
        # Public (non-private)
        self.brand = brand
        # Private
        self.__model = model

    # Getter for private variable
    def get_model(self):
        return self.__model

# Object creation
my_car = Car("Toyota", "Corolla")

print("PUBLIC (Non-Private)")
print(my_car.brand)          # ✅ direct access allowed
my_car.brand = "Honda"       # ✅ modification allowed
print(my_car.brand)

print("\nPRIVATE (Encapsulation)")
print(my_car.get_model())    # ✅ access via method

# ❌ Uncommenting below line will give error
# print(my_car.__model)
