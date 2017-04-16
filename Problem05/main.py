# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# SOLUTION
# Brute :/
# 232792560

number = 2520

while True:
    number += 20
    divisible = True
    i = 6
    while True:
        i += 1
        if number%(i+2) != 0:
            divisible = False
            break
        if i == 20:
            break

    if divisible:
        print(number)
        break
    if number%10000000 == 0:
        print("Already checked: %d" % number)
