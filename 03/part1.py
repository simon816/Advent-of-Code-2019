import sys

grid = []

for i in range(40000):
    grid.append([0] * 40000)

lineid = 0

intersections = []

for line in sys.stdin.readlines():
    lineid += 1
    x, y = 20000, 20000
    for step in line.strip().split(','):
        ox, oy = x, y
        dir = step[0]
        dist = int(step[1:])
        if dir == 'U':
            y += dist
        elif dir == 'R':
            x += dist
        elif dir == 'D':
            y -= dist
        elif dir == 'L':
            x -= dist
        assert x > 0 and x < 40000
        assert y > 0 and y < 40000
        for p in range(min(ox, x), max(ox, x) + 1):
            if grid[p][oy] != 0 and grid[p][oy] != lineid:
                intersections.append((p, oy))
            grid[p][oy] = lineid
        for p in range(min(oy, y), max(oy, y) + 1):
            if grid[ox][p] != 0 and grid[ox][p] != lineid:
                intersections.append((ox, p))
            grid[ox][p] = lineid
        
print(intersections)
norm = [((x - 20000), (y - 20000)) for x, y in intersections]
print(norm)
print(min(abs(x) + abs(y) for x, y in norm if x + y != 0))
