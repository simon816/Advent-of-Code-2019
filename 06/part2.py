import sys

nodes = {}
parents = {}

you_node = None
san_node = None

for line in sys.stdin.readlines():
    left, right = line.strip().split(')')
    if left not in nodes:
        nodes[left] = set()
    nodes[left].add(right)
    if right not in nodes:
        nodes[right] = set()
    assert right not in parents
    parents[right] = left
    if right == 'YOU':
        you_node = left
    elif right == 'SAN':
        san_node = left

p = you_node

path_to_you = []
path_to_san = []

while p != 'COM':
    p = parents[p]
    path_to_you.append(p)
path_to_you.reverse()

p = san_node
while p != 'COM':
    p = parents[p]
    path_to_san.append(p)
path_to_san.reverse()

shift = 0
for node in path_to_you:
    if len(path_to_san) > shift and path_to_san[shift] == node:
        shift += 1
    else:
        break

print(len(path_to_san[shift:]) + len(path_to_you[shift:]) + 2)
