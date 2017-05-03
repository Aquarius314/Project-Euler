import math

primes = [2, 3]
number = 3

max_range = 1000000

while len(primes) < max_range:
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
        if len(primes)%1000 == 0:
            print("Ilosc liczb pierwszych: %d" % len(primes))
