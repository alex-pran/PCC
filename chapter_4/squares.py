squares = []
for numbers in range(1,11):
    square = numbers ** 2
    squares.append(square)

print(f"squares - {squares}")

odd_squares = []
for digits in list(range(2,11,2)):
    square_a = digits ** 2
    odd_squares.append(square_a)

print(f"odd squares - {odd_squares}")

sq = []
for nums in range(1,11):
    sq.append(nums ** 2)

print(sq)