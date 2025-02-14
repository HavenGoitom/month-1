class Vehicle:
    def __init__(self, make , model, plate_num, price):
        self.make = make
        self.model = model
        self.__plate_num = plate_num
        self._price = price
    def describe(self):
        print(f"This is a {self.make} {self.model} with plate number {self.__plate_num} and price {self._price}")
class Bike(Vehicle):
    def __init__ (self, make, model, plate_num, price, bike_type):
        super().__init__(make, model, plate_num, price)
        self.bike_type = bike_type
    def describe(self):
        print(f"This is a {self.make} {self.model} with plate number {self._Vehicle__plate_num} and price {self._price} and is a {self.bike_type} bike")
class Car(Vehicle):
    def __init__ (self, make, model, plate_num, price, num_doors):
        super().__init__(make, model, plate_num, price)
        self.num_doors = num_doors
    def describe(self):
        print(f"This is a {self.make} {self.model} with plate number {self._Vehicle__plate_num} and price {self._price} and has {self.num_doors} doors")

vehicle1 = Vehicle("Toyota", "Corolla", "ABC123", 1000000)
vehicle1.describe()
bike1 = Bike("Yamaha", "R1", "DEF456", 2000000, "sports")
bike1.describe()
car1 = Car("Toyota", "Corolla", "GHI789", 3000000, 4)
car1.describe()

# if you want to acess the private attribute __plate_num, you can use the following code

print(vehicle1._Vehicle__plate_num) 