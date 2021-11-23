
# Simple dictionary
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
print("------------------------------------------------")
newAge = cat_1['age'] = 2
print(cat_1['age'])
print(cat_1)
print("------------------------------------------------")
cat_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position {cat_3['x_position']}")

if cat_3['speed'] == 'slow':
    x_increment = 1

elif cat_3['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

cat_3['x_position'] = cat_3['x_position'] + x_increment

print(f"New x_position {cat_3['x_position']}")
print("------------------------------------------------")

# A dictionary of similar Objects
favorite_food = {
    'Tom': 'potato',
    'Kate': 'watermelon',
    'Michael': 'banana',
    'Bobby': 'avocado'
}

print(favorite_food)
print(favorite_food['Bobby'])
print(favorite_food['Kate'])

food = favorite_food['Tom'].title()
print(food)
