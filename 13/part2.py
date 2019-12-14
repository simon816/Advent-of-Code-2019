import sys
import itertools
import curses

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

inputfile = sys.argv[1]
with open(inputfile, 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

inputs = []
prog = run_code(data, inputs)

tile_map = {
    0: ' ',
    1: '#',
    2: '=',
    3: '_',
    4: 'o'
}

data[0] = 2

with open('keys.txt', 'r') as f:
    keys = [int(k) for k in f.read().strip().split(',')]

presses = []

def main(stdscr):
    score = 0
    while True:
        stdscr.addstr(0, 50, str(score))
        stdscr.refresh()
        try:
            wait, val = next(prog)
        except StopIteration:
            break
        if wait == WAI_OUT:
            x = val
            _, y = next(prog)
            _, tile = next(prog)
        else:
            if len(keys):
                val = keys.pop(0)
            else:
                key = stdscr.getch()
                if key == curses.KEY_LEFT:
                    val = -1
                elif key == curses.KEY_RIGHT:
                    val = 1
                else:
                    val = 0
            inputs.append(val)
            presses.append(val)
            continue
        if x == -1 and y == 0:
            score = tile
            continue
        stdscr.addstr(y, x, tile_map[tile])
    return score


from curses import wrapper
print(wrapper(main))
with open('keys.txt', 'w') as f:
    f.write(','.join(map(str, presses[:-35])))
