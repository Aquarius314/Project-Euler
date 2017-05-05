import time
import math
start_time = time.time()


total_sum = 0
for num in range(3, 100000):
    partial_sum = 0
    snum = str(num)
    for d in snum:
        partial_sum += math.factorial(int(d))
    if partial_sum == num:
        total_sum += num
    if num%1000==0:
        print("Checking %d, current sum: %d" % (num, total_sum))

print(total_sum)

print("Time: %d milliseconds" % int(time.time()*1000-start_time*1000))
