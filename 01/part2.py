import sys

def calc(input):
    val = (input // 3) - 2
    if val <= 0:
        return 0
    return val + calc(val)

if __name__ == '__main__':

    total = 0
    for line in sys.stdin.readlines():
        mass = int(line.strip())
        total += calc(mass)

    print(total)
