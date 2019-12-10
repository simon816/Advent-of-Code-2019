import sys
import itertools

traces = []

for trace in sys.stdin.readlines():
    minmaxes = []
    x, y = 0, 0
    for step in trace.strip().split(','):
        dir = step[0]
        dist = int(step[1:])
        xoff, yoff = 0, 0
        if dir == 'U':
            yoff = dist
        elif dir == 'R':
            xoff = dist
        elif dir == 'D':
            yoff = -dist
        elif dir == 'L':
            xoff = -dist
        oldx, oldy = x, y
        x, y = x + xoff, y + yoff
        minmax = ((min(oldx, x), max(oldx, x)), (min(oldy, y), max(oldy, y)), dir)
        minmaxes.append(minmax)
    traces.append(minmaxes)

intersections = []

def cross_intersect(hy, hx1, hx2, vx, vy1, vy2):
    # Greater than max or less than min
    if vx > hx2 or vx < hx1:
        return
    if hy > vy2 or hy < vy1:
        return
    intersections.append((vx, hy))

def line_intersect(l1min, l1max, l2min, l2max, l1oth, l2oth, mk):
    if l1oth != l2oth:
        return
    if l1min > l2max or l1max < l2min:
        return
    start = max(l1min, l2min)
    end = min(l1max, l2max)
    intersections.extend(mk(l1oth, val) for val in range(start, end + 1))

for (l1minx, l1maxx), (l1miny, l1maxy), l1d in traces[0]:
    for (l2minx, l2maxx), (l2miny, l2maxy), l2d in traces[1]:
        if l1d == 'U' or l1d == 'D':
            if l2d == 'L' or l2d == 'R':
                cross_intersect(l2miny, l2minx, l2maxx, l1minx, l1miny, l1maxy)
            else:
                line_intersect(l1miny, l1maxy, l2miny, l2maxy, l1minx, l2minx,
                               lambda x, y: (x, y))
        else:
            if l2d == 'U' or l2d == 'D':
                cross_intersect(l1miny, l1minx, l1maxx, l2minx, l2miny, l2maxy)
            else:
                line_intersect(l1minx, l1maxx, l2minx, l2maxx, l1miny, l2miny,
                               lambda y, x: (x, y))

print(intersections)
print(min(abs(x) + abs(y) for x, y in intersections if x or y))
