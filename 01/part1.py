import sys

if __name__ == '__main__':

    total = 0
    for line in sys.stdin.readlines():
        mass = int(line.strip())
        fuel = (mass // 3) - 2
        total += fuel

    print(total)
