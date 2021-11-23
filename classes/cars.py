class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0
        self.miles = 0

    def get_description(self):
        print(f"This is {self.make.title()} {self.model.title()} "
              f"{self.year}.")

    def get_mileage(self):
        print(f"Car has {self.__mileage} miles on it.")

    def set_mileage(self, new_mileage):
        if new_mileage > self.__mileage:
            self.__mileage = new_mileage
            print("Odometer reader update.")
        else:
            print("Odometer reader was not updated.")

    def increment_odometer(self, miles):
        if miles > self.__mileage:
            self.__mileage = miles
            print("Odometer reader update")
        else:
            print("Odometer reader was not updated")

