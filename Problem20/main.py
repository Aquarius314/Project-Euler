import math
num = str(math.factorial(100))
digit_sum = 0
for c in num:
    digit_sum += int(c)
print(digit_sum)
