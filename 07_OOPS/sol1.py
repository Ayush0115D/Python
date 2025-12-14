#about classes and objects in Py
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
        
        #q2
    def full_name(self):
        return f"{self.brand} {self.model}"
   #q3     
class ElectricCar(Car):
        def __init__(self, brand, model, battery_size):
            super().__init__(brand, model)
            self.battery_size = battery_size

         
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
