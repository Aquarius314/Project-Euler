import data

# ASCII: -64 for ord(char) gives alphabetical position (for uppercase)

names = sorted(data.names)
names_score = []

for i in range(len(names)):
    char_sum = 0
    for c in names[i]:
        char_sum += ord(c)-64
    names_score.append(char_sum*(i+1))

print(sum(names_score))
