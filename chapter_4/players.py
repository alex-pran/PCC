players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])

print(players[2:])
print(players[-3:])
print(players[-2:])


print("\n----------------")

print("Here are first three players on my team:")
for player in players[:2]:
    print(player.title())