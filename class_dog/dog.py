class Dog:
    """ A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} roled over.")

my_dog = Dog('Fluffy', 4)
my_dog.sit()
my_dog.roll_over()
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age}.")