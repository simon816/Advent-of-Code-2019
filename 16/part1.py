import sys
import itertools

initial = list(map(int, sys.stdin.read().strip()))

def repeat_each(pattern, n):
    for elem in pattern:
        yield from itertools.repeat(elem, n)

def fft(inlist):
    for round in range(len(inlist)):
        patcycle = repeat_each(itertools.cycle([0, 1, 0, -1]), round + 1)
        next(patcycle) # Skip first
        total = 0
        for val in inlist:
            total += val * next(patcycle)
        digit = abs(total) % 10
        yield digit

curr = initial
for _ in range(100):
    curr = list(fft(curr))

print(''.join(map(str, curr[:8])))
