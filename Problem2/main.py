# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms

# SOLUTION
# 1. Implement iterating Fibonacci numbers algorithm
# 2. Add each even numbers
# 3. Stop when any number exceed 4M
# 4. The answer is 4613732

import math

prev1 = 0               # first previous
prev2 = 1               # last previous
fib = prev1 + prev2     # current fibonacci number
even_sum = 0


while fib < 4000000:
    prev1 = prev2
    prev2 = fib
    fib = prev1 + prev2
    if fib%2 == 0:
        even_sum += fib

print("Result is: %d" % even_sum)
