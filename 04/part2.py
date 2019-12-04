count = 0
for candidate in range(372304, 847060 + 1):
    n = candidate
    prev = None
    discard = False
    double = None
    reject = set()
    allow = False
    for i in range(6):
        n, m = divmod(n, 10)
        if prev is not None and m > prev:
            discard = True
            break
        if m == double:
            reject.add(m)
            double = None
        elif m == prev and m not in reject:
            double = m
        elif double is not None and m != double:
            allow = True
        prev = m
    if discard or (double is None and not allow):
        continue
    assert n == 0
    count += 1

print(count)
