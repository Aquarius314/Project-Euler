import math


def is_prime(number):
    if number < 2:
        return False
    correct = True
    p = 2
    while p <= math.sqrt(number):
        if number%p == 0:
            correct = False
            break
        p += 1
    return correct


def primes_range(max_range):

    primes = [2, 3]
    number = 3
    while number+2 <= max_range:
        number += 2
        is_prime = True
        for p in primes:
            if number%p == 0:
                is_prime = False
                break
            if p >= math.sqrt(number):
                break
        if is_prime:
            primes.append(number)

    return primes

maxxx = 999999

p = primes_range(maxxx)

print(len(p))

p_sum = 0
max_length = 0
the_prime = 0

for i in range(len(p)):
    p_sum = 0
    length = 0
    for j in range(i, len(p)):
        length += 1
        p_sum += p[j]
        if p_sum > maxxx:
            break
        if is_prime(p_sum) and length > max_length:
            max_length = length
            the_prime = p_sum

print("Longest chain is %d-long for prime: %d" % (max_length, the_prime))
