import sys

layers = []

row = []
rows = []
for val in sys.stdin.read().strip():
    row.append(val)
    if len(row) == 25:
        rows.append(row)
        row = []
    if len(rows) == 6:
        layers.append(rows)
        rows = []

assert not row
assert not rows

def count(layer, digit):
    return sum(row.count(digit) for row in layer)

layer = min(layers, key=lambda layer: count(layer, '0'))

print(count(layer, '1') * count(layer, '2'))
