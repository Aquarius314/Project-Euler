# Lattice paths

# Printing
def print_square(s):
    for r in s:
        line_str = ""
        for value in r:
            line_str += str(value)
            line_str += " "
        print(line_str)
    return

square = []
n = 20
n += 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    square.append(row)

# Initial value
square[0][0] = 1

# Printing
print_square(square)

print("After injecting correct values:")
for i in range(n):
    for j in range(n):
        if i > 0:
            square[i][j] += square[i-1][j]
        if j > 0:
            square[i][j] += square[i][j-1]

print_square(square)

print("The answer is %d" % square[n-1][n-1])
