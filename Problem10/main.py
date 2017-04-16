# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# SOLUTION
# 1. Erastothenes' Sieve algorithm to find primes below 2M
# 2. Add them

import math

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

primes_sum = 0
for p in primes_range(2000000):
    primes_sum += p

print(primes_sum)
