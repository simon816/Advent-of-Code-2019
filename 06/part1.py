import sys

nodes = {}

for line in sys.stdin.readlines():
    left, right = line.strip().split(')')
    if left not in nodes:
        nodes[left] = set()
    nodes[left].add(right)
    if right not in nodes:
        nodes[right] = set()

totals = {}

def do_node(node):
    local_total = totals[node]
    children = nodes[node]
    for child in children:
        assert child not in totals
        totals[child] = local_total + 1
        do_node(child)

totals['COM'] = 0
do_node('COM')

print(sum(totals.values()))
    
