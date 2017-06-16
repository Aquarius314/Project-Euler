def is_pandigital9(number):
    if len(str(number)) < 9:
        return False
    if '0' in str(number):
        return False
    snum = sorted(str(number))
    for i in range(len(snum)-1):
        if snum[i] == snum[i+1]:
            return False
    return True

def product(number, integers):
    snum = ""
    for i in integers:
        snum += str(number*i)
    return snum

biggest = 0

# printing the biggest as it appears bigger than the biggest found already
num = 1
while True:
    num += 1
    # integers 1 to 9 loop:
    for i in range(1, 5):
        n_list = []
        for j in range(1, i):
            n_list.append(j)
        p = product(num, n_list)
        if is_pandigital9(p):
            if biggest < p:
                biggest = p
                print(str(p) + " from " + str(num) + " and " + str(n_list))
                # wait for keyboard interrupt
        if p > 10**9:
            continue
