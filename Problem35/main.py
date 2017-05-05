import math
import time
start_time = time.time()

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

def is_prime(number):
    # additional conditions:
    if number == 2 or number == 5:
        return True
    if str(number)[0] == 0:
        return False
    l = number%10
    if l%5==0 or l%2==0:
        return False
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


def combinations(number):
    combs = []  # to w Pythonie deklaracja nowej tablicy
    for n in number:    # petla foreach dla wszystkich znaczkow w liczbie
        new_combs = []  # tablica po nowej iteracji
        for c in combs: # foreach dla kazdej kombinacji z poprzedniej iteracji
            for i in range(len(c)+1):   # petla dla kazdego miejsca w danej kombinacji
                new_combs.append(c[0:i]+n+c[i:len(c)])  # dodajemy nowa kombinacje z literka
        combs = new_combs   # podmieniamy liste kombinacji na nowe

        if len(combs) == 0: # jesli lista kombinacji jest pusta, dodajemy pierwszy znak
            combs.append(n)
    combs = sorted(combs)
    return combs

def circular(number):
    combs = []
    for i in range(len(number)):
        number = number[1:len(number)]+number[0]
        combs.append(number)
    return combs

# combs = combinations("1114")
# i = 1
# for num in combs:
#     print("Combination %2d:   %s" % (i, num))
#     i += 1


primes = primes_range(1000000)

cirs = 0
circular_primes = []

iterations = 0
for p in primes:
    iterations += 1
    prime_combs = circular(str(p))
    all_primes = True
    for c in prime_combs:
        if not is_prime(int(c)):
            # remove all circulars from primes
            for cir in prime_combs:
                if cir in primes:
                    primes.remove(cir)
            all_primes = False
            break
    if all_primes:
        cirs += len(prime_combs)
        for c in prime_combs:
            if c in primes:
                primes.remove(c)
        if p not in circular_primes:
            circular_primes.append(p)
            print("Another circular found: %d" % p)

print("There are %d circular primes below 1M" % len(circular_primes))

print("Time: %d milliseconds" % int(time.time()*1000-start_time*1000))
