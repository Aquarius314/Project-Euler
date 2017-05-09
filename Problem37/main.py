import math

# We can stop after 11 truncatable primes found
# because it is said that there are only 11 of them

def is_prime(number):
    number = int(number)
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

def is_trunc(number):
    snum = str(number)
    for i in range(1, len(snum)):
        left = snum[i:len(snum)]
        right = snum[0:i]
        if not is_prime(left):
            return False
        if not is_prime(right):
            return False
    return True

primes = [2, 3, 5, 7]
number = 9

truncs = []

while len(truncs) < 11:
    number += 2
    prime = True
    for p in primes:
        if number%p == 0:
            prime = False
            break
        if p >= math.sqrt(number):
            break
    if prime:
        primes.append(number)
        if is_trunc(number):
            truncs.append(number)
            print("%d truncs found, last: %d" % (len(truncs), number))

print(sum(truncs))
