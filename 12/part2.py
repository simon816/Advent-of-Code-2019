import sys
import itertools

moons = []

for line in sys.stdin.readlines():
    moon = dict(c.strip().split('=') for c in line.strip()[1:-1].split(','))
    moon = [int(moon[c]) for c in 'xyz']
    moons.append({'p': moon, 'v': [0, 0, 0]})

states = set()

def step(comp):
    apply_gravity(comp)
    apply_velocity(comp)

def gravity_change(a, b):
    if a == b:
        return 0, 0
    return (1, -1) if a < b else (-1, 1)

def apply_gravity(comp):
    for m1, m2 in itertools.combinations(moons, 2):
        p1, p2 = m1['p'], m2['p']
        v1x, v2x = gravity_change(p1[comp], p2[comp])
        m1['v'][comp] += v1x
        m2['v'][comp] += v2x

def apply_velocity(comp):
    for m in moons:
        m['p'][comp] += m['v'][comp]


def get_for_comp(comp):
    n = 0
    start_state = tuple((m['v'][comp], m['p'][comp]) for m in moons)
    state = None
    while True:
        if state == start_state:
            break
        step(comp)
        state = tuple((m['v'][comp], m['p'][comp]) for m in moons)
        n += 1
    return n

x = get_for_comp(0)
y = get_for_comp(1)
z = get_for_comp(2)

from math import gcd
lcm = x
for i in (y, z):
    lcm = int(lcm * i / gcd(lcm, i))
print(lcm)
