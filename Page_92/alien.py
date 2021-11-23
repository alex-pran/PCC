alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


print("########################")

new_points = alien_0['points']
print(f"You just earned {new_points} points")

print("########################")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print()
print("########### Starting with empty dictionary #############")
# Starting with empty dictionary

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print()
print("########### Modifying Values in a Dictionary #############")

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

print()
print("########### (GAME) #############")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position {alien_0['x_position']}")

# Move the alien to the right
# Determine ow far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_incremnt = 3

else:
    # This must be a fast alien
    x_increment = 4

# The new position is  the old position plus the increment

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position : {alien_0['x_position']}")

print()
print("########### (Removing key-value pairs) #############")



