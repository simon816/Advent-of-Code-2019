import sys
import itertools

sizes = {
    1: 3, # ADD a b r
    2: 3, # MUL a b r
    3: 1, # IN d
    4: 1, # OUT p
    5: 2, # JNZ t d
    6: 2, # JZ t d
    7: 3, # LT a b r
    8: 3, # EQ a b r
    9: 1, # ARB b
}

WAI_IN, WAI_OUT = range(2)

def run_code(data, inputs):

    rel_base = 0

    def expand(addr):
        if addr >= len(data):
            data.extend(0 for _ in range(1 + addr - len(data)))

    def read(addr):
        expand(addr)
        return data[addr]

    def decode(*params, write=False):
        for mode, val in params:
            if mode == 0:
                if write:
                    yield val
                else:
                    yield read(val)
            elif mode == 1:
                assert not write
                yield val
            elif mode == 2:
                if write:
                    yield rel_base + val
                else:
                    yield read(rel_base + val)
            else:
                assert False

    def write(addr, val):
        expand(addr)
        data[addr] = val

    ptr = 0
    while data[ptr] != 99:
        insn = data[ptr]
        modes, opcode = divmod(insn, 100)
        params = []
        for n in range(sizes[opcode]):
            modes, mode = divmod(modes, 10)
            param = data[ptr + n + 1]
            params.append((mode, param))
        # print(data[ptr:ptr + sizes[opcode] + 1], opcode, params)

        if opcode == 1:
            a, b = decode(*params[:2])
            r, = decode(params[2], write=True)
            write(r, a + b)
        elif opcode == 2:
            a, b = decode(*params[:2])
            r, = decode(params[2], write=True)
            write(r, a * b)
        elif opcode == 3:
            if not inputs:
                yield (WAI_IN, None)
            addr, = decode(params[0], write=True)
            write(addr, inputs.pop(0))
        elif opcode == 4:
            out, = decode(params[0])
            yield (WAI_OUT, out)
        elif opcode == 5:
            t, d = decode(*params)
            if t != 0:
                ptr = d
                continue
        elif opcode == 6:
            t, d = decode(*params)
            if t == 0:
                ptr = d
                continue
        elif opcode == 7:
            a, b = decode(*params[:2])
            r, = decode(params[2], write=True)
            write(r, 1 if a < b else 0)
        elif opcode == 8:
            a, b = decode(*params[:2])
            r, = decode(params[2], write=True)
            write(r, 1 if a == b else 0)
        elif opcode == 9:
            off, = decode(params[0])
            rel_base += off
        else:
            assert False

        ptr += sizes[opcode] + 1

data = list(map(int, sys.stdin.read().strip().split(',')))

opp = [None, 2, 1, 4, 3]

class Node:

    def __init__(self, parent, parent_dir):
        self.adj = {1: None, 2: None, 3: None, 4: None}
        if parent_dir is not None:
            assert parent is not None
            self.adj[parent_dir] = parent
        self.parent = parent_dir
        self.wall = False

    def choose_next(self):
        for dir, node in self.adj.items():
            if node is None:
                self.adj[dir] = node = Node(self, opp[dir])
                return dir, node
        return self.parent, self.adj[self.parent]

    def fully_explored(self):
        return all(self.adj.values())

    def parent_count(self):
        if self.parent is None:
            return 0
        return 1 + self.adj[self.parent].parent_count()

    def set_wall(self):
        self.wall = True

    def clear_node(self, node):
        clear = set()
        for k, v in self.adj.items():
            if v == node:
                clear.add(k)
        for k in clear:
            del self.adj[k]

    def get_available(self):
        for node in self.adj.values():
            if node is None or node.wall:
                continue
            node.clear_node(self)
            yield node

curr = start = Node(None, None)

origin = None

while True:
    inputs = []
    prog = run_code(data, inputs)
    wai, _ = next(prog)
    assert wai == WAI_IN
    dir, new_node = curr.choose_next()
    inputs.append(dir)
    wai, status = next(prog)
    assert wai == WAI_OUT
    if status != 0:
        curr = new_node
        if status == 2:
            origin = curr
    if curr is start and curr.fully_explored():
        break

front = [origin]
depth = 0
while front:
    front = [node for p in front for node in p.get_available()]
    depth += 1

# -2 for some reason
print(depth - 2)
