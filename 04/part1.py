count = 0
for candidate in range(372304, 847060 + 1):
    n = candidate
    prev = None
    discard = False
    repeat = False
    for i in range(6):
        n, m = divmod(n, 10)
        if prev is not None and m > prev:
            discard = True
            break
        if m == prev:
            repeat = True
        prev = m
    if discard or not repeat:
        continue
    assert n == 0
    count += 1

print(count)
