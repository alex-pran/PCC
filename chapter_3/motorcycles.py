motorcycles =  ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati') #"value".append(add name in list)
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[2] = 'bianco'
print(motorcycles)


car_brand = []

car_brand.append('subaru')
car_brand.append('honda')
car_brand.append('toyota')
car_brand.append('ram')

print(car_brand)
print(car_brand[3])
print(f"\n{car_brand}")
print(f"\n\t{car_brand[1]}")
print(f"\n{car_brand[3]}")

print(car_brand)

car_brand.insert(0, 'bmw') # name.instert(0), - add text in to the list
print(car_brand)

del car_brand[4] #remove item in list
print(car_brand)
print(f"\n\n++++++++++++++++++++++++++++++++")

popped_car_brand = car_brand.pop()
print(car_brand)
print(popped_car_brand)

print(f"\n\n++++++++++++++++++++++++++++++++")

my_list = [1,2,3,4,5]
last = my_list.pop()
print(last)

four = my_list.pop(-1)
print(four)

three = my_list.pop(-2)
print(three)

two = my_list.pop(-3)
print(two)

one = my_list.pop(-4)
print(one)