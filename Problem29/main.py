# 2 <= a <= 100, 2 <= b <= 100

terms = []

for a in range(2, 101):
    for b in range(2, 101):
        term = a**b
        if term not in terms:
            terms.append(term)
            # control info
            if len(terms)%100 == 0:
                print("%d terms found, checking a=%d, b=%d" % (len(terms), a, b))

print(len(terms))
