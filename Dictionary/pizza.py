# Pizza store
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'five chees']
}

print(pizza)

# Summarize order
print(f"You ordered a {pizza['crust']} - crust pizz "
      f"with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


# Tacos oreder
tacos = {
    'tacos_1': 'beef',
    'tacos_2': 'chicken',
    'tacos_3': 'shrimp',
    'tacos_4': 'fish',
    'add': ['onion', 'avocado', 'cream sour']
}

print(tacos)

print(f"Your ordered a {tacos['tacos_3']} taco with the following add:")

for taco in tacos['add']:
    print(f"\t{taco}")