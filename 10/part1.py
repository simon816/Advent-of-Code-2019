import sys

grid = []

for line in sys.stdin.readlines():
    grid.append(list(line.strip()))
    

detections = []

locations = []

locset = set()

for y, row in enumerate(grid):
    for x, thing in enumerate(row):
        if thing == '#':
            locations.append((x, y))
            locset.add((x, y))

def fp_close_to(f, i):
    sub = f - i
    return sub > -0.00001 and sub < 0.00001

def calc(x, y):
    count = 0
    for ox, oy in locations:
        blocked = False
        if ox == x and oy == y:
            continue
        (x1, y1), (x2, y2) = sorted(((x, y), (ox, oy)))
        if x1 == x2:
            yoff = 1 if y < oy else -1
            for ystep in range(y + yoff, oy, yoff):
                if (x, ystep) in locset:
                    blocked = True
                    break
            if not blocked:
                count += 1
            continue
        slope = (y1 - y2) / (x1 - x2)
        ystep = y1
        for xstep in range(x1 + 1, x2):
            ystep += slope
            intval = round(ystep)
            if fp_close_to(ystep, intval) and (xstep, intval) in locset:
                blocked = True
                break
        if blocked:
            continue
        count += 1
    return count


for x, y in locations:
    detections.append(calc(x, y))

print(max(detections))
