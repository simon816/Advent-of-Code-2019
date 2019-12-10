import sys
import math

grid = []

for line in sys.stdin.readlines():
    grid.append(list(line.strip()))
    

detections = []

locations = []

for y, row in enumerate(grid):
    for x, thing in enumerate(row):
        if thing == '#':
            locations.append((x, y))

def fp_close_to(f, i):
    sub = f - i
    return sub > -0.00001 and sub < 0.00001

def get_visible(x, y, locations, locset):
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
                yield ox, oy
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
        yield ox, oy

locset = set(locations)

def get_count(x, y):
    return sum(1 for _ in get_visible(x, y, locations, locset))

for x, y in locations:
    detections.append((get_count(x, y), x, y))

_, originx, originy = max(detections, key=lambda p: p[0])

polar = {}
for x, y in locations:
    dx = x - originx
    dy = y - originy
    t = math.atan2(dy, dx) + (math.pi / 2)
    if t < 0:
        t += 2 * math.pi
    polar[(x, y)] = t

count = 0
while True:
    visible = get_visible(originx, originy, polar.keys(), polar.keys())
    order = sorted([(polar[(x, y)], x, y) for x, y in visible],
                   key=lambda c: c[0])
    if not order:
        break
    for _, x, y in order:
        del polar[(x, y)]
        count += 1
        if count == 200:
            print((x * 100) + y)
            break
