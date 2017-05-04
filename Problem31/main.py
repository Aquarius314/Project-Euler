# 2Pound in how many ways?
# 1p 2p 5p 10p 20p 50p 100p 200p

changes = 0
i = 0

for p200 in range(200/200 + 1):
    for p100 in range(200/100 + 1):
        for p50 in range(200/50 + 1):
            for p20 in range(200/20 + 1):
                for p10 in range(200/10 + 1):
                    for p5 in range(200/5 + 1):
                        for p2 in range(200/2 + 1):
                            change = p200*200+p100*100+p50*50+p20*20+p10*10+p5*5+p2*2
                            i += 1
                            if change > 200:
                                break
                            else:
                                changes += 1


print(changes)
print(i)
