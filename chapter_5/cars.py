cars = ['bmw', 'lexus', 'ferrari', 'honda']

for car in cars:
    print(f"I love {car} a lot.")
print(cars[2])

### shortcut to autoformat: ctrl + alt + l

print("####################################")
pizzas = ['pepperoni', 'mushrooms', 'cheese', 'grandma']

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print('I really love pizzaaaaaa.')

print("############################")
animals = ['cat', 'dog', 'horse']

for animal in animals[:]:
    print(f" A {animal} will a great pet.")
print("Any of these animals would make a great pet!")

print("############## copy of animals ##############")

new_animals = animals
print(f"copy_animals list: {new_animals}")
print(f"animal list: {animals}")
new_animals.append('snake')
print(f"copy_animals list: {new_animals}")
print(f"animals list :{animals}")