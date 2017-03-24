# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# SOLUTION
# 1. Approximate target sqrt
# 2. Search by Erastothenes' Sieve for all primes less than target sqrt
# 3. Find first prime in list which is factor of target (starting from the biggest)
# 4. The answer is 6857

import math

target_number = 600851475143
target_sqrt = math.sqrt(target_number)
# add 1 for sure
target_sqrt += 1

primes = [2]

number = 3
while True:
    is_prime = True

    for p in primes:
        if number%p == 0:
            is_prime = False
        if p*p >= number:
            break   # surely one of pair-factors cannot be bigger than sqrt

    if is_prime:
        primes.append(number)

    number += 2

    if number > target_sqrt:
        break


# search for biggest factor in primes list
for p in reversed(primes):
    if target_number%p == 0:
        print("Biggest prime factor is %d" % p)
        break
