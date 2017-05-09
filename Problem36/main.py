# Palindromic number in both 10 and 2 base
# Find the sum of all of them below 1M

def is_pal(number):
    snum = str(number)
    for i in range(len(snum)):
        if snum[i] != snum[len(snum)-i-1]:
            return False
    return True

def to_binary(number):
    return "{0:b}".format(number)

total_sum = 0

for number in range(10**6):
    if is_pal(number):
        if is_pal(to_binary(number)):
            total_sum += number

print(total_sum)
