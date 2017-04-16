# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Difference between them is 2640
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

# BRUTE
# Solution is 25164150

squared_sum = 0
sum_squares = 0

for i in range(100):
    squared_sum += i+1
    sum_squares += (i+1)**2

squared_sum = squared_sum**2

print(squared_sum - sum_squares)
