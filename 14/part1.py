import sys

def qty_split(s):
    spl = s.strip().split(' ')
    return int(spl[0]), spl[1]

dependencies = {}

for line in sys.stdin.readlines():
    input, output = line.strip().split('=>')
    inputs = [qty_split(elem) for elem in input.split(',')]
    out_qty, out = qty_split(output)
    assert out not in dependencies
    dependencies[out] = (out_qty, inputs)

residue = {}

def produce(elem):
    get_qty, depends = dependencies[elem]
    for d_qty, d_elem in depends:
        acquire(d_elem, d_qty)
    if elem in residue:
        residue[elem] += get_qty
    else:
        residue[elem] = get_qty

ore_count = 0

def acquire(elem, qty):
    if elem == 'ORE':
        global ore_count
        ore_count += qty
        return
    if elem not in residue:
        residue[elem] = 0
    while residue[elem] < qty:
        produce(elem)
    residue[elem] -= qty
    
acquire('FUEL', 1)
print(ore_count)
