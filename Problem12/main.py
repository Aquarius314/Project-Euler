# What is the value of the first triangle number to have over 500 divisors?

# SOLUTION
# 1. In loop, consecutively:
# 2. Search for triangle number
# 3. Count it's divisors
# 4. Every divisor below sqrt is symmetrical so add 2 for each
# 5. Finish at sqrt
# 6. Repeat until divisors number is above 500
# 7. The answer is 76576500 after 5853 ms

import math
import time

start_time = time.time()

i = 1
number = 1
max_div = 0

while True:
    i += 1
    number += i
    divisors = 0
    for j in range(int(math.floor(math.sqrt(number))+1)):
        if number%(j+1) == 0:
            divisors += 1
            if j != math.sqrt(number):
                divisors += 1
            else:
                break
    if divisors > max_div:
        max_div = divisors
        print("Number %d is: %d, divisors: %d" % (i, number, divisors))
    if divisors >= 500:
        print(number)
        break

print("Time: %d milliseconds" % int(time.time()*1000-start_time*1000))
