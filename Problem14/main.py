# Collatz sequence
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)


import time
start_time = time.time()

sequences = {1 : 1}

for number in range(10000000):
    n = number+1
    seq_num = 0
    while n != 1:
        if n%2 == 0:    # even
            n = n/2
        else:   # uneven
            n = 3*n+1
        seq_num += 1
        if n in sequences:
            sequences[number+1] = seq_num+sequences[n]
            # print("%d needs %d steps, stopped after %d" % (number+1, seq_num+sequences[n], seq_num))
            break

max_seq = 0
longest_chain = 1

for number in sequences:
    if sequences[number] > max_seq:
        max_seq = sequences[number]
        longest_chain = number

print("Number that gives longest chain is %d with chain: %d" % (longest_chain, max_seq))

print("Time: %d milliseconds" % int(time.time()*1000-start_time*1000))
