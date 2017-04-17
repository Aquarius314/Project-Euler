# Sum of multiples of 3 and 5 below 1000?
# 233168

multiples_sum = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        multiples_sum += i

print(multiples_sum)
