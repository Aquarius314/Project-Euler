# 28123 is upper limit
up = 28123

# 1. Find all abundant numbers below 28123
abundants = []

for number in range(up):
    divisors_sum = 0
    for div in range(number/2+1):
        if div == 0:
            continue
        if number%(div) == 0:
            divisors_sum += div
    if divisors_sum > number:
        abundants.append(number)

print("All abundant numbers found: %d" % len(abundants))

# 2. Find all numbers below 100 that cannot be made of two abundant numbers

numbers = []

for number in range(up):
    for a in abundants:
        if (number-a) in abundants:
            break
        if a > number:
            numbers.append(number)
            if len(numbers)%100 == 0:
                print("Numbers len: %d, checking: %d" % (len(numbers), number))
            break

print(sum(numbers))
