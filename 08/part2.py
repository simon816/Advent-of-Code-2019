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

final = []

for y in range(6):
    row = []
    for x in range(25):
        for layer in layers:
            px = layer[y][x]
            if px != '2':
                break
        row.append(px)
    final.append(row)

print('\n'.join(''.join(row) for row in final).replace('0', '.'))
