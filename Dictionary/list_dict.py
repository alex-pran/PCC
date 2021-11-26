alien_0 = {'color': 'red', 'points':5}
alien_1 = {'color': 'blue', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("====================================")
aliens = []

# Make 30 green aliens
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# # Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# #Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

