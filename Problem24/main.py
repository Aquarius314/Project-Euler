
perms = []


# snum = "0123456789"
# perms.append(int(snum))
# while True:
#     intnum = int(snum)
#     intnum += 1
#     # does it start with zero?
#     is_zero = snum[0] == '0'
#
#
#
# snum = "000123"
# is_zero = snum[0] == '0'
# print(snum)
# intnum = int(snum)
# intnum += 1
# snum = str(intnum)
# if is_zero:
#     snum = '0' + snum
# print(snum)

num = 2013456789

power = 9*8*7*6*5*4*3*2 # number of perms starting with 0
power = power*2         # double for starting with 0 or 1

perms.append(num)

while len(perms) <= 1000000-power:
    num += 1
    snum = sorted(str(num))
    uniq = True
    for i in range(len(snum)-1):
        if snum[i] == snum[i+1]:
            uniq = False
            break
    if uniq:
        perms.append(num)
        if len(perms)%100 == 0:
            complete = 100.0*len(perms)/(1000000-power)
            print("%d perms found, checking: %d." % (len(perms), num))
            print("Completed: %f" % complete)

print(perms[len(perms)-1])
print(perms[len(perms)-2])
print(perms[len(perms)-3])
