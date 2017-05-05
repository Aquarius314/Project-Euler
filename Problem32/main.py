import time

start_time = time.time()


def all_digits(a, b, c):
    digits = []
    str_num = str(a) + str(b) + str(c)
    for d in str_num:
        if d == '0':
            return False
        if d not in digits:
            digits.append(d)
        else:
            return False
    return len(digits) == 9

uniqs = []

for a in range(1, 10000):
    for b in range(a, 10000):
        c = a*b
        if all_digits(a, b, c):
            if c not in uniqs:
                uniqs.append(c)
                print("%d uniqs found, checking: %d, %d" % (len(uniqs), a, b))
    if a%100 == 0:
        print("Cheking a=%d" % a)

print(sum(uniqs))

print("Time: %d milliseconds" % int(time.time()*1000-start_time*1000))
