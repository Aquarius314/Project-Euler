import time
start_time = time.time()

i = 0
while True:
    i += 1
    print(i)
    if i > 100000000:
        break

print("Time: %d milliseconds" % int(time.time()*1000-start_time*1000))
