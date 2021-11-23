# x = 1           #int
# y = 2.25        #float
# name = 'Bond'   #str
# is_cool = True  #boolean

x, y, name, is_cool = (1, 2.5, 'Bond', True)
a = x + y
print(a,name, is_cool)

print("\n ######################")
print()


# Casting

x = str(x)
y = int(y)
z = float(y)

print(type(y), z)


# String

name = "Brad"
age = 37

#Concatenate
print('My name is '+ name + ' ' + str(age))

#Argument by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-String (python 3.6+)
print(f"My name is {name}, and I am {age}")


# String methods

s = 'hello world'

#Capitalize string
print(s.capitalize())

#Make all uppercase
print(s.upper())

#Make all lower
print(s.lower())

#Swap case
print(s.swapcase())

#Get lenght
print(len(s))

#Find possitiom
print(s.find('r'))

#Is all alphabetic
print(s.isalpha())

#Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
#Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

#Get a value
print(fruits[1])
print(len(fruits))
fruits.append('Mango')
print(fruits)
fruits.remove('Grapes')
print(fruits)


#Dictionary
person = {
    'first_name': 'James',
'last_name': 'Bond',
'age': 37}

print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

#get dict keys
print(person.keys())

#Get dict items
print(person.items())

#print(person)

#copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

#Remove item
del(person2['age'])
person2.pop('phone')
print(person2)

#Clear

person2.clear()
print(person2)


#Get lenght
print(len(person))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
print(people)
print(people[1]['name'])
print(people[0])
print(people[0]['age'])

