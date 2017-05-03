# ERATOSTHENES' SIEVE ALGORITHM FOR PRIME NUMBERS

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


def primes_quantity(max_quantity):

    primes = [2, 3]
    number = 3
    while len(primes) < max_quantity:
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
