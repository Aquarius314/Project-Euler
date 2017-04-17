
import data

triangle = data.triangle

maximum = 0

for i in range(len(triangle)):

    for j in range(i):

        try:
            left = triangle[i-1][j-1]
        except Error:
            left = 0
        try:
            right = triangle[i-1][j]
        except Error:
            right = 0

        triangle[i][j] += max(left, right)

    if i > 0:
        triangle[i][i] += triangle[i-1][i-1]

maximum = max(triangle[len(triangle)-1])

print(maximum)
