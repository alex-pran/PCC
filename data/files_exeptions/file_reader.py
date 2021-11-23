with open('.././../data/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

print()
print("####### rstrip() #######")
print()

with open('.././../data/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

print()
print("####### line #######")
print()

with open('.././../data/pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

print()
print("####### line.rstrip() #######")
print()

with open('.././../data/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

