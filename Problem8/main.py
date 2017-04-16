

# 1. Divide number for smaller numbers, dividing at each zeros
# 2. Delete all numbers shorter than 13 digits
# 3. Check for product inside every number
# Solution is 23514624000

number = [\
'7316717653133', '624919225119674426574742355349194934\
9698352', '3127745', '6326239578318', '169848', '1869478851843\
8586156', '7891129494954595', '17379583319528532', '88', '5511\
1254', '698747158523863', '5', '71569329', '963295227443', '43557\
6689664895', '4452445231617318564', '3', '98711121722383113\
6222989342338', '3', '81353362766142828', '6444486645238749\
3', '3589', '729629', '49156', '44', '77239', '71381', '5158593', '796', '866\
7', '1724271218839987979', '87922749219', '169972', '888', '93776\
65727333', '1', '5336788122', '2354218', '975125454', '594752243\
525849', '771167', '556', '136', '48395864467', '6324415722155397\
53697817977846174', '6495514929', '862569321978468622482\
83972241375657', '56', '5749', '2614', '79729686524145351', '474\
8216637', '4844', '319989', '889524345', '658541227588666881\
1642717147992444292823', '863465674813919123162824586\
178664583591245665294765456828489128831426', '769', '42\
24219', '22671', '556263211111', '937', '5442175', '694165896', '4', '8\
', '71984', '385', '96245544436298123', '9878799272442849', '9188\
8458', '156166', '979191338754992', '524', '6368991256', '7176', '6\
', '58861164671', '94', '5', '77541', '22569831552', '55935729725\
7163626956188267', '4282524836', '82325753', '42', '75296345']

series = []

print("First optimization: %d elements" % len(number))
for n in number:
    print(n)

new_number = []

for fragment in number:
    if len(fragment) >= 13:
        new_number.append(fragment)

print('')
print("Second optimization: %d elements" % len(new_number))
for n in new_number:
    print(n)

print('')
print("Finding biggest product of adjacent numbers:")

biggest = 0
index = 0   #
nnn = 0   #
for num in new_number:
    i = 0
    for i in range(len(num)-12):
        product = 1
        for j in range(13):
            product *= int(num[j+i])
        if product > biggest:
            biggest = product
            nnn = int(num)
            index = i

print("Biggest product: %d" % biggest)
print("For number: %d, from: %d" % (nnn, index))

# product = 1
# for c in num:
#     product *= int(c)
# if product > biggest:
#     biggest = product
