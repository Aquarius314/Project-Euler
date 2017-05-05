
# Printing
def print_square(s):
    for r in s:
        line_str = ""
        for value in r:
            if value == 1:
                line_str += "o"
            else:
                line_str += " "
            line_str += " "
        print(line_str)
    return

square = []
n = 40

for i in range(n):
    row = []
    for j in range(n-i):
        row.append(0)
    square.append(row)

# Initial value
square[0][0] = 1

# Printing
print_square(square)

print("After injecting correct values:")
for i in range(n):
    for j in range(n):
        if j < len(square[i]):
            if i > 0:
                square[i][j] += square[i-1][j]
            if j > 0:
                square[i][j] += square[i][j-1]
            square[i][j] = square[i][j]%2

print_square(square)

# print("The answer is %d" % square[n-1][n-1])
