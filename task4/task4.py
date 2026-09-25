import sys

with open(sys.argv[1], 'r') as f:
    nums = []

    for line in f:
        nums.append(int(line))

min_moves = 1000000

for number in nums:
    moves = 0

    for num in nums:
        if num > number:
            moves += num - number
        else:
            moves += number - num

    if moves < min_moves:
        min_moves = moves

if min_moves <= 20:
    print(min_moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")