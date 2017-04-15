# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers

# SOLUTION
# 1. Iterate from 100 to 999 for 2 loops
# 2. Second loop value starts from first loop value
#    to avoid duplicated combinations
# 3. Check if the product is palindrome
# 4. Compare with the biggest received so far
# 5. The answer is 906609 (for 893*813)

import math

biggest_palindrome = 0

up = 999    # should be 999
down = 100  # should be 100

for i in range(up - down):
    for j in range(up - down):
        product = (i+down)*(j+down)
        # check if it is palindrome
        product_str = str(product)
        is_palindrome = True
        for c in range(len(product_str)/2):
            if product_str[c] != product_str[len(product_str)-c-1]:
                is_palindrome = False
                break

        if is_palindrome:
           if product > biggest_palindrome:
               biggest_palindrome = product

print("Biggest: %d" % biggest_palindrome)
