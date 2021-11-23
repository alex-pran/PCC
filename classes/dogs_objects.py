# Chapter 9
# Object-oriented programming - modeling the real world object and using them in program
#Class - model of something; generic state (description) and behavior of object (car, pet, tree, etc..)
# Object
from classes.dogs import Dog, Cat

class Dog():
   #behavior(поведение): run(), sit(), bark()
    def __init__(self, name, color, breed, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    def run(self):
        print(f'{self.name.title()} is running....')

    def sit(self):
        print(f'{self.name.title()} dog is sitting :)')

    def bark(self):
        print(f'{self.name.title()} woof woof!!!')

    def description(self):
        print(f"\nHi this is {self.name}. \nI am a beautiful {self.color} color"
              f"\nMy breed {self.breed}. \nI am {self.age} old")



dog1 = Dog('Krish', 'white', 'American eskimo', 6) #instantiation

# __init__ - function is automatically called (executed)
# dog1 - jbject; instance of Dog class
# (krish, white, american escimo) - instance variables

print('name of the dog:',dog1.name)
print('color of the dog:',dog1.color)
print('breed of the dog:',dog1.breed)
print('age of the dog:',dog1.age)

def dog(self):
    print(f"Name of the dog: {dog1.name}")
    print(f"Color of the dog: {dog1.color}")
    print(f"Breedal of the dog: {dog1.breed}")


print('# --------------------')
dog1.run()
dog1.bark()
dog1.sit()
dog1.description()


dog2 = Dog(age = 6, breed = 'French Bulldog',
           color = 'Black', name = 'Avni')

dog3 = Dog('jak', 'brown', 'boerboel', 7)

print('dog2')
dog2.run()
dog2.bark()
dog2.sit()
dog2.description()

print('dog3')
dog3.run()
dog3.bark()
dog3.sit()
dog3.description()

print("###################################")
print("\n")

class Restaurant():
    pass
    #restaurant_name, cuisine_type
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        # describe restsursnt

    def describe_restaurant(self):
        print(f"We are ' {self.restaurant_name} 'and we are {self.cuisine_type} restaurant")


    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} are open")

restaurant = Restaurant('TacoBell', 'mexican')
restaurant.restaurant_name
restaurant.cuisine_type
restaurant.describe_restaurant()
restaurant.open_restaurant()