people3 = ['John', 'Paul', 'Sara', 'Susan']

#Simple for loop

for person in people3:
    print(f'Current Person: {person}')


print('#######')
#Break

# for person in people3:
#     if person == 'Sara':
#         break
#     print(f'Current Person: {person}')

print('#########')

#Continue / skip 'Sara'

for person in people3:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')
print('###########3')
#Range

# for i in range(len(people3)):
#     print(people3[i])
#
# for i in range(0, 11):
#     print(f'Number: {i}')

#while loops

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1