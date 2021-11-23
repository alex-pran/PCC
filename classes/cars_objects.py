from classes.cars import *

car1 = Car('toyota', 'camry', 2021)
print(car1.make)
print(car1.model)
print(car1.year)
car1.get_description()

car1.get_mileage()
car1.mileage = 25
car1.get_mileage()
#car1.mileage = -25
car1.set_mileage(-5)
car1.get_mileage()
car1.set_mileage(24)
car1.get_mileage()
print("-----------------------------------")
car1.increment_odometer(50)
car1.get_mileage()
car1.increment_odometer(-10) #not possible in real world
car1.get_mileage()

car2 = Car('tesla', 'model x', 2022)