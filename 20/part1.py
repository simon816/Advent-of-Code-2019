import sys
from collections import defaultdict
import re

top_labels = []

middle_lines = []

bottom_labels = []
bottom_y = 0

portals = defaultdict(list)

all_lines = list(sys.stdin.readlines())

map_lines = []

for i, line in enumerate(all_lines):
    y = i - 2 # Top two lines
    left_label = line[:2]
    right_label = line[-3:-1]
    main = line[2:-3]
    # Check for left/right labels
    if left_label != '  ':
        portals[left_label].append((0, y))
    if right_label != '  ':
        portals[right_label].append((len(main) - 1, y))
    # Read top labels
    if len(top_labels) < 2:
        top_labels.append(main)
        continue
    # Read bottom labels
    if i >= len(all_lines) - 2:
        bottom_labels.append(main)
        if not bottom_y:
            bottom_y = y - 1
        continue
    # Read main map
    map_lines.append(main)
    if any(c >= 'A' and c <= 'Z' for c in main):
        middle_lines.append((y, main))

def read_labels(labels, y):
    for i, c in enumerate(labels[0]):
        if c >= 'A' and c <= 'Z':
            second = labels[1][i]
            name = c + second
            portals[name].append((i, y))

read_labels(top_labels, 0)
read_labels(bottom_labels, bottom_y)

middle_left_re = re.compile('([.][A-Z]{2}) +')
middle_right_re = re.compile(' +([A-Z]{2}[.])')

middle_top = []
middle_top_y = 0
middle_bottom = []
middle_bottom_y = 0

for y, line in middle_lines:
    m1 = middle_left_re.search(line)
    if m1:
        x = m1.start(1)
        portals[m1.group(1)[1:]].append((x, y))
    m2 = middle_right_re.search(line)
    if m2:
        x = m2.end(1) - 1
        portals[m2.group(1)[:-1]].append((x, y))
    if not m1 and not m2:
        if len(middle_top) < 2:
            middle_top.append(line)
            if not middle_top_y:
                middle_top_y = y - 1
        else:
            middle_bottom.append(line)
            middle_bottom_y = y + 1

read_labels(middle_top, middle_top_y)
read_labels(middle_bottom, middle_bottom_y)

start_pos = dest_pos = None
portal_edges = {}

for label, locs in portals.items():
    if label == 'AA':
        assert len(locs) == 1
        start_pos = locs[0]
    elif label == 'ZZ':
        assert len(locs) == 1
        dest_pos = locs[0]
    else:
        assert len(locs) == 2
        assert locs[0] not in portal_edges
        assert locs[1] not in portal_edges
        portal_edges[locs[0]] = locs[1]
        portal_edges[locs[1]] = locs[0]

nodes = {}

class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adj = set()

    def add_edge(self, x, y):
        other = nodes[(x, y)]
        self.adj.add(other)
        other.adj.add(self)

    def __repr__(self):
        return 'Node(%d, %d)' % (self.x, self.y)

for y, line in enumerate(map_lines):
    for x, c in enumerate(line):
        if c == '.':
            nodes[(x, y)] = Node(x, y)
            if (x - 1, y) in nodes:
                nodes[(x - 1, y)].add_edge(x, y)
            if (x, y - 1) in nodes:
                nodes[(x, y - 1)].add_edge(x, y)

assert start_pos in nodes
assert dest_pos in nodes

for p1, p2 in portal_edges.items():
    nodes[p1].add_edge(*p2)

permanents = set()
weights = {}
src = nodes[start_pos]
dest = nodes[dest_pos]
curr_dist = 0
node = src
while node != dest:
    weights[node] = curr_dist
    permanents.add(node)
    adj = node.adj
    for a in adj:
        if a in permanents:
            continue
        if a in weights:
            weights[a] = min(weights[a], curr_dist + 1)
        else:
            weights[a] = curr_dist + 1
    non_perms = list(filter(lambda e: e[0] not in permanents, weights.items()))
    assert non_perms, "No Route!"
    lowest = min(map(lambda e: e[1], non_perms))
    matching = filter(lambda e: e[1] == lowest, non_perms)
    node = next(matching)[0]
    curr_dist += 1
permanents.add(dest)
weights[dest] = curr_dist
node = dest
path = []
while node != src:
    permanents.remove(node)
    path.append(node)
    dist = weights[node]
    perm_adj = list(filter(lambda a: a in permanents, node.adj))
    lowest = min(map(lambda n: weights[n], perm_adj))
    matching = filter(lambda n: weights[n] == lowest, perm_adj)
    node = next(matching)

print(len(path))
