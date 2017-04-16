# what is the 10 001st prime number?

# SOLUTION
# 1. Erastothenes' Sieve: use 2 and 3 as base two primes
# 2. Check every 2-consecutive number for dividing by previous primes
#    which are equal or lower than square root of that number
# 3. Find 10001 of them
# Solution is 104743

import math

primes = [2, 3]
number = 3

while len(primes) < 10001:
    number += 2
    is_prime = True
    for p in primes:
        if number%p == 0:
            is_prime = False
            break
        if p > math.sqrt(number):
            break
    if is_prime:
        primes.append(number)

print(primes[10000])
