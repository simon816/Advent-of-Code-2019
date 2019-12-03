import sys

grid = []

for i in range(40000):
    grid.append([None] * 40000)

lineid = 0

intersections = []

for line in sys.stdin.readlines():
    lineid += 1
    x, y = 20000, 20000
    counter = 1
    for step in line.strip().split(','):
        ox, oy = x, y
        dir = step[0]
        dist = int(step[1:])
        move_x = False
        neg = False
        if dir == 'U':
            y += dist
        elif dir == 'R':
            x += dist
            move_x = True
        elif dir == 'D':
            y -= dist
            neg = True
        elif dir == 'L':
            x -= dist
            neg = True
            move_x = True
        assert x > 0 and x < 40000
        assert y > 0 and y < 40000
        counter -= 1
        if neg:
            counter += dist
        if move_x:
            for p in range(min(ox, x), max(ox, x) + 1):
                g = grid[p][oy]
                exists = False
                if g is not None:
                    exists = lineid in g
                    if not exists:
                        intersections.append((p, oy))
                else:
                    grid[p][oy] = {}
                oldc = g[lineid] if exists else counter
                grid[p][oy][lineid] = min(counter, oldc)
                if neg:
                    counter -= 1
                else:
                    counter += 1
        else:
            for p in range(min(oy, y), max(oy, y) + 1):
                g = grid[ox][p]
                exists = False
                if g is not None:
                    exists = lineid in g
                    if not exists:
                        intersections.append((ox, p))
                else:
                    grid[ox][p] = {}
                oldc = g[lineid] if exists else counter
                grid[ox][p][lineid] = min(counter, oldc)
                if neg:
                    counter -= 1
                else:
                    counter += 1
        if neg:
            counter += dist + 2

print(intersections)
counts = [grid[x][y] for x, y in intersections if x != 20000 and y != 20000]
print(counts)
print(min(sum(c.values()) for c in counts))
