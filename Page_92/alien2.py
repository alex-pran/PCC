alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

print("------------------------------------------------")

print(alien_0['color'])
print(alien_0['points'])

print("------------------------------------------------")

print(alien_0['color'])

print("------------------------------------------------")

new_points = alien_0['points']
print(f"You got {new_points} points")
print(f"You have {alien_0['color']} color")

print("------------------------------------------------")

cat_1 = {'name': 'Fox', 'color': 'red', 'age': 4}
cat_2 = {'name': 'Fluffy', 'color': 'black_white', 'age': 4.5}

print(cat_1)
print(cat_2)

print("------------------------------------------------")

print(cat_1['name'])
print(cat_2['name'])

print("------------------------------------------------")

new_name = cat_2['name'] = 'Tom'
print(cat_2['name'])
print(cat_2)

newAge = cat_1['age'] = 2
print(cat_1['age'])
print(cat_1)