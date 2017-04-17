# 1. Count divisors
# d[a] = sum of proper divisors of a

d = []

for i in range(10000):
    d.append(0)
    for j in range(i/2+1):
        if j == 0:
            continue
        if i%j == 0:
            d[i] += j

# 2. Check if d[a] = b <=> d[b] = a

amicable_sum = 0

for a in range(len(d)):
    if d[a] < len(d) and d[d[a]] == a and d[a] != a:
        amicable_sum += a

print(amicable_sum)
