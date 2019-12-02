import sys

data = list(map(int, sys.stdin.read().strip().split(',')))

data[1] = 12
data[2] = 2

ptr = 0
while data[ptr] != 99:
    a = data[data[ptr + 1]]
    b = data[data[ptr + 2]]
    r = data[ptr + 3]
    if data[ptr] == 1:
        data[r] = a + b
    elif data[ptr] == 2:
        data[r] = a * b
    else:
        assert False
    ptr += 4
print(data[0])
