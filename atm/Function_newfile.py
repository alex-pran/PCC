# Part 1

def sayHello(name):
    print(f'Hello {name}')
sayHello('John Doe')


# part 2

def sayHell(name2 = 'Sam'):
    print(f'Hello{name2}')
sayHell()

#part 3

def getSum(num1, num2):
    total = num1 + num2
    return total

#print(getSum(1, 2))  remember
sum = (getSum(2,2))
print(sum)#another way

#lambda

getSum = lambda num1, num2: num1 + num2
print(getSum(10,3))