# What is the sum of the digits of 2^1000?

# Brutal solution using Python's possibilities

num = str(2**1000)

digit_sum = 0

for c in num:
    digit_sum += int(c)

print(digit_sum)
