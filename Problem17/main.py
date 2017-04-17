# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?

# 21124

below_20 = [
'' ,
'one' ,
'two' ,
'three' ,
'four' ,
'five' ,
'six' ,
'seven' ,
'eight' ,
'nine' ,
'ten' ,
'eleven' ,
'twelve' ,
'thirteen' ,
'fourteen' ,
'fifteen' ,
'sixteen' ,
'seventeen' ,
'eighteen' ,
'nineteen'
]

decimal = [
'twenty' ,
'thirty' ,
'forty' ,
'fifty' ,
'sixty' ,
'seventy' ,
'eighty' ,
'ninety'
]

def convert_to_written(number):
    name = ""
    number_str = str(number)
    if number == 1000:
        name += "one thousand"
        # print(name)
        return name
    if number >= 100:
        name += below_20[int(number_str[0])]
        name += " hundred"
        number = number%100
        if number > 0:
            name += " and "
        number_str = str(number)

    if number < 20:
        name += below_20[number%20]
        # print(name)
    else:
        name += decimal[int(number_str[0])-2] +" "+ below_20[int(number_str[1])]
        # print(name)
    return name

def cut_spaces(word):
    new_word = ""
    for c in word:
        if c != ' ':
            new_word += c
    # print(new_word + " = " + str(len(new_word)))
    return new_word

letters = 0

for i in range(1000):
    letters += len(cut_spaces(convert_to_written(i+1)))

print(letters)
