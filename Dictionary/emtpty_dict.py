
# Empty dictionary
alien_0 = {}

# Add items in dictionary
alien_0['color'] = 'red'
alien_0['points'] = 5

# Change color
alien_0['color'] = 'yellow'

print(alien_0)


a = [['moskva', 123], ['perm', 456], ['omsk', 789]]
#b = dict(a)
print(a)
#print(b)


print("==================================")

person = {}
s = "ivanov petrov sidorov samara sgu 4 5 6 7 8 9"
s = s.split()
person['firstName'] = s[0]
person['midName'] = s[1]
person['lastName'] = s[2]
person['city'] = s[3]
person['university'] = s[4]
person['marks'] = []

for i in s[5:]:
    person['marks'].append(int(i))

print(s)
print(person)
