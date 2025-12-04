# https://projecteuler.net/problem=17

num_word_map = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def letter_count(number):
    str_number = str(number)

    if len(str_number) == 1:
        letters = len(num_word_map[number])        

    elif len(str_number) == 2:
        if number not in num_word_map:
            letters = len(num_word_map[int(str_number[0]) * 10]) + len(num_word_map[int(str_number[1])])
        else:
            letters = len(num_word_map[number])        

    elif len(str_number) == 3:
        letters = len(num_word_map[int(str_number[0])]) + len("hundredand")

        if int(str_number[1:3]) not in num_word_map:
            if int(str_number[1]) == 0 and int(str_number[2]) != 0:
                letters += len(num_word_map[int(str_number[2])])
            elif int(str_number[1]) == 0 and int(str_number[2]) == 0:
                letters -= len("and")
            else:
                letters += len(num_word_map[int(str_number[1]) * 10]) + len(num_word_map[int(str_number[2])])
        else:
            letters += len(num_word_map[int(str_number[1:3])])

    else:
        letters = len("onethousand")        

    return letters

LETTER_SUM = 0
for num in range(0, 1000):
    LETTER_SUM += letter_count(num + 1)

print(LETTER_SUM)
# 21124
