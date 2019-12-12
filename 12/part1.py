import sys
import itertools

moons = []

for line in sys.stdin.readlines():
    moon = dict(c.strip().split('=') for c in line.strip()[1:-1].split(','))
    moon = tuple(int(moon[c]) for c in 'xyz')
    moons.append({'p': moon, 'v': (0, 0, 0)})

def step():
    apply_gravity()
    apply_velocity()

def gravity_change(a, b):
    if a == b:
        return 0, 0
    return (1, -1) if a < b else (-1, 1)

def apply_gravity():
    for m1, m2 in itertools.combinations(moons, 2):
        p1, p2 = m1['p'], m2['p']
        v1x, v2x = gravity_change(p1[0], p2[0])
        v1y, v2y = gravity_change(p1[1], p2[1])
        v1z, v2z = gravity_change(p1[2], p2[2])
        m1['v'] = vec_add(m1['v'], (v1x, v1y, v1z))
        m2['v'] = vec_add(m2['v'], (v2x, v2y, v2z))

def apply_velocity():
    for m in moons:
        m['p'] = vec_add(m['p'], m['v'])
        
def vec_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2])

def pot_energy(m):
    return sum(map(abs, m['p']))

def kin_energy(m):
    return sum(map(abs, m['v']))

def tot_energy(m):
    return pot_energy(m) * kin_energy(m)

for _ in range(1000):
    step()

print(sum(map(tot_energy, moons)))
