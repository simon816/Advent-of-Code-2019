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

residue = {k: 0 for k in dependencies.keys()}
residue['ORE'] = 100000000

count = 0

def produce(elem):
    if elem == 'ORE':
        print(count)
        exit(0)
    get_qty, depends = dependencies[elem]
    for d_qty, d_elem in depends:
        acquire(d_elem, d_qty)
    residue[elem] += get_qty

def acquire(elem, qty):
    while residue[elem] < qty:
        produce(elem)
    residue[elem] -= qty

"""
while True:
    acquire('FUEL', 1)
    count += 1
"""

print("#include <stdlib.h>\n#include <stdio.h>")

print("int count = 0;")

print("""long int residue_ORE = 1000000000000;
void acquire_ORE(int qty) {
    residue_ORE -= qty;
    if (residue_ORE < 0) {
        printf("%d\\n", count);
        exit(0);
    }
}""")

for k in dependencies.keys():
    print('void produce_%s();' % k)
    print('void acquire_%s(int qty);' % k)

for k, (q, deps) in dependencies.items():
    acq = '\n'.join('    acquire_%s(%d);' % (d, dq) for (dq, d) in deps)
    print("""int residue_%s = 0;
void produce_%s() {
%s
    residue_%s += %d;
}

void acquire_%s(int qty) {
    while (residue_%s < qty) {
        produce_%s();
    }
    residue_%s -= qty;
}
""" % (k, k, acq, k, q, k, k, k, k))

print("""int main(int argc, char *argv[]) {
    while (1) {
        acquire_FUEL(1);
        count++;
    }
    return 0;
}
""")
