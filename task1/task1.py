import sys

def get_path(n, m):
    path = ""
    current = 1

    while True:
        path += str(current)
        current += m-1

        if current > n:
            current -= n

        if current == 1:
            break

    return path

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

path1 = get_path(n1, m1)
path2 = get_path(n2, m2)

print(path1 + path2)