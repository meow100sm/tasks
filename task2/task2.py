import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'r') as f1:
    center = f1.readline().split()
    radius = f1.readline().split()

x0 = float(center[0])
y0 = float(center[1])

a = float(radius[0])
b = float(radius[1])

with open(file2, 'r') as f2:
    for line in f2:
        point = line.split()
        x = float(point[0])
        y = float(point[1])
        result = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)

        if result == 1:
            print(0)
        elif result < 1:
            print(1)
        else:
            print(2)