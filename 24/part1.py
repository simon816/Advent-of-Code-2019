import sys
from copy import deepcopy

seen = set()

layout = [[c for c in line.strip()] for line in sys.stdin.readlines()]

seen.add(str(layout))

while True:

    new_layout = deepcopy(layout)

    for x in range(5):
        for y in range(5):
            own = layout[y][x]
            adj_bug = 0
            if x > 0 and layout[y][x - 1] == '#':
                adj_bug += 1
            if x < 4 and layout[y][x + 1] == '#':
                adj_bug += 1
            if y > 0 and layout[y - 1][x] == '#':
                adj_bug += 1
            if y < 4 and layout[y + 1][x] == '#':
                adj_bug += 1
            if own == '#' and adj_bug != 1:
                own = '.'
            elif own == '.' and (adj_bug == 1 or adj_bug == 2):
                own = '#'
            new_layout[y][x] = own

    state = str(new_layout)
    if state in seen:
        flat = [v for row in new_layout for v in row]
        print(sum(2**i if v == '#' else 0 for i, v in enumerate(flat)))
        break
    seen.add(state)
    layout = new_layout
