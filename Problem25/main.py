
digits = 10**999

i = -1
fib1 = -1
fib2 = 1
fib = 1
while True:
    i += 1
    fib = fib2 + fib1
    fib1 = fib2
    fib2 = fib
    if fib >= digits:
        print("%dth is: %d" % (i, fib))
        break
