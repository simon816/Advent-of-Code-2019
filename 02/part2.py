import sys

orig_data = list(map(int, sys.stdin.read().strip().split(',')))

def do(data):

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
    return data[0]

for n in range(100):
    for v in range(100):
        data = list(orig_data)
        data[1] = n
        data[2] = v
        if do(data) == 19690720:
            print((100 * n) + v)
            exit(1)

assert False
