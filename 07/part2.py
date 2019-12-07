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
}

WAI_IN, WAI_OUT = range(2)

def run_code(data, inputs):

    def decode(*params):
        for mode, val in params:
            if mode == 0:
                yield data[val]
            elif mode == 1:
                yield val
            else:
                assert False

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
            data[params[2][1]] = a + b
        elif opcode == 2:
            a, b = decode(*params[:2])
            data[params[2][1]] = a * b
        elif opcode == 3:
            if not inputs:
                yield (WAI_IN, None)
            data[params[0][1]] = inputs.pop(0)
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
            data[params[2][1]] = 1 if a < b else 0
        elif opcode == 8:
            a, b = decode(*params[:2])
            data[params[2][1]] = 1 if a == b else 0
        else:
            assert False

        ptr += sizes[opcode] + 1

data = list(map(int, sys.stdin.read().strip().split(',')))

values = []

for perm in itertools.permutations(range(5, 10)):
    instances = []
    inputs = []
    for setting in perm:
        ins = [setting]
        inputs.append(ins)
        instances.append(run_code(list(data), ins))
    val = 0
    stop = False
    while not stop:
        for inst, ins in zip(instances, inputs):
            ins.append(val)
            try:
                io_block, out = next(inst)
                assert io_block == WAI_OUT
                val = out
            except StopIteration:
                stop = True
                break
        values.append(val)

print(max(values))
