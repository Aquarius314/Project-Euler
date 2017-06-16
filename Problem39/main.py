

combs = []

max_c = 0
for p in range(1001):
    combs.append(0)
    for a in range(1, int(p/2)):
        for b in range(1, a):
            c = p - (a+b)
            s = sorted([a, b, c])
            _a = s[0]
            _b = s[1]
            _c = s[2]
            if _a**2 + _b**2 == _c**2:
                combs[p] += 1
    if combs[p] > max_c:
        max_c = combs[p]
        print("Max so far: %d, for: %d" % (max_c, p))

print(combs[120])
