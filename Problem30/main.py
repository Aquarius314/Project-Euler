# sum of fifth powers of number's digits

num = 10

total_sum = 0
quantity = 0

while True:
    num += 1
    snum = str(num)
    powers_sum = 0
    for n in snum:
        power = int(n)**5
        powers_sum += power
    if powers_sum == num:
        quantity += 1
        total_sum += num
        print("%d number found: %d. Total sum: %d" % (quantity, num, total_sum))

    if num > 10**6:
        break
