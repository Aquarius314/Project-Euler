# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
# a^2 + b^2 = c^2
# Find a pythagorean triplet for which a + b + c = 1000
# Find their product

# SOLUTION
# 1. Find all triplets with sum lower than 1000
# 2. No need to check when c < b or c < a or a < b
# 3. Choose only pythagorean triplets from them
# 4. There is only 1 triplet with that conditions. Multiply it
# 5. The answer is 31875000

triplets = []

for a in range(1000):
    for b in range(1000-(a+2)):
        if a < b:
            break
        c = 1000-(a+1)-(b+1)
        if c < b:
            break
        if c < a:
            break
        triplets.append([a+1, b+1, c])

pyt_triplets = []

for t in triplets:
    c = max(t)
    sum_squares = 0
    for num in t:
        if num is not c:
            sum_squares += num**2
    if c**2 == sum_squares:
        pyt_triplets.append(t)

print(pyt_triplets)
product = 1
for num in pyt_triplets[0]:
    product *= num
print(product)
print("Algo info:")
print("Triplets len: %d" % len(triplets))
print("Pyt_triplets len: %d" % len(pyt_triplets))
