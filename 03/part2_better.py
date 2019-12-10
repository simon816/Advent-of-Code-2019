import sys
import itertools

traces = []

for trace in sys.stdin.readlines():
    minmaxes = []
    start_off = 0
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
        minmax = ((min(oldx, x), max(oldx, x)),
                  (min(oldy, y), max(oldy, y)),
                  dir, start_off)
        minmaxes.append(minmax)
        start_off += dist
    traces.append(minmaxes)

intersections = {}

def intersect(pos, vals):
    if pos in intersections:
        old = intersections[pos]
        # Use min to get first intersection
        vals[1] = min(old[1], vals[1])
        vals[2] = min(old[2], vals[2])
    intersections[pos] = vals

def cross_intersect(hy, hx1, hx2, vx, vy1, vy2, hs, vs, t1, t2):
    # Greater than max or less than min
    if vx > hx2 or vx < hx1:
        return
    if hy > vy2 or hy < vy1:
        return
    deltax, deltay = vx - hx1, hy - vy1
    hsteps = hs(deltax)
    vsteps = vs(deltay)
    intersect((vx, hy), {t1: vsteps, t2: hsteps})

def line_intersect(l1min, l1max, l2min, l2max, l1oth, l2oth, mk, l1sh, l2sh, t1, t2):
    if l1oth != l2oth:
        return
    if l1min > l2max or l1max < l2min:
        return
    start = max(l1min, l2min)
    end = min(l1max, l2max)
    for val in range(start, end + 1):
        l1steps = l1sh(val)
        l2steps = l2sh(val)
        intersect(mk(l1oth, val), {t1: l1steps, t2: l2steps})

def shift(s, d, l):
    return lambda o: s + o if d in 'UR' else (s + l) - o

for (l1minx, l1maxx), (l1miny, l1maxy), l1d, l1s in traces[0]:
    for (l2minx, l2maxx), (l2miny, l2maxy), l2d, l2s in traces[1]:
        if l1d == 'U' or l1d == 'D':
            l1sh = shift(l1s, l1d, l1maxy - l1miny)
            if l2d == 'L' or l2d == 'R':
                l2sh = shift(l2s, l2d, l2maxx - l2minx)
                cross_intersect(l2miny, l2minx, l2maxx,
                                l1minx, l1miny, l1maxy,
                                l2sh, l1sh, 2, 1)
            else:
                l2sh = shift(l2s, l2d, l2maxy - l2miny)
                line_intersect(l1miny, l1maxy,
                               l2miny, l2maxy,
                               l1minx, l2minx,
                               lambda x, y: (x, y),
                               l1sh, l2sh, 1, 2)
        else:
            l1sh = shift(l1s, l1d, l1maxx - l1minx)
            if l2d == 'U' or l2d == 'D':
                l2sh = shift(l2s, l2d, l2maxy - l2miny)
                cross_intersect(l1miny, l1minx, l1maxx,
                                l2minx, l2miny, l2maxy,
                                l1sh, l2sh, 1, 2)
            else:
                l2sh = shift(l2s, l2d, l2maxx - l2minx)
                line_intersect(l1minx, l1maxx,
                               l2minx, l2maxx,
                               l1miny, l2miny,
                               lambda y, x: (x, y),
                               l1sh, l2sh, 1, 2)

del intersections[(0, 0)]

print(min(sum(d.values()) for d in intersections.values()))
