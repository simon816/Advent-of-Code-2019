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

prog = run_code(data, [])

screen = {}

while True:
    sl = list(itertools.islice(prog, 3))
    if not sl:
        break
    (_, x), (_, y), (_, tile) = sl
    screen[(x, y)] = tile

print(sum(1 for tile in screen.values() if tile == 2))
