
rows = []

n = 1001

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    rows.append(row)

x = int(n/2)
y = int(x)

# ver = 1 # vertical steps
# hor = 1 # horizontal steps
steps = 0
horizontal = True
step_limit = 1

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_index = 0
cur_dir = dirs[dir_index]

rows[x][y] = 1
for i in range(1, n**2):
    if step_limit == steps:
        if horizontal:
            horizontal = False
            steps = 0
        else:
            steps = 0
            step_limit += 1
            horizontal = True
        dir_index = (dir_index+1)%4
        cur_dir = dirs[dir_index]
    x += cur_dir[0]
    y += cur_dir[1]
    steps += 1
    rows[x][y] = i+1

# for r in rows:
#     str_row = ""
#     for num in r:
#         str_row += " "
#         if num < 10:
#             str_row += " "
#         str_row += str(num)
#     print(str_row)

diag_sum = -1

for i in range(len(rows)):
    diag_sum += rows[i][i]
    diag_sum += rows[i][len(rows)-1-i]

print(diag_sum)
