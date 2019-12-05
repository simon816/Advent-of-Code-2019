import sys

sizes = {
    1: 3, # ADD a b r
    2: 3, # MUL a b r
    3: 1, # IN
    4: 1, # OUT
}

def run_code(data, inputs, outputs):

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
            data[params[0][1]] = inputs.pop(0)
        elif opcode == 4:
            out, = decode(params[0])
            outputs.append(out)
        else:
            assert False

        ptr += sizes[opcode] + 1

data = list(map(int, sys.stdin.read().strip().split(',')))

outputs = []
run_code(data, [1], outputs)
print(outputs)
