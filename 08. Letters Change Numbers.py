words = input().split()

total_sum = 0

def letter_alphabet_possition(letter):
    position = 0
    if letter.isupper():
        position = ord(letter) - 64
    else:
        position = ord(letter) - 96
    return position

for word in words:
    word_points = 0
    number = int(word[1:-1])
    if word[0].isupper():
        word_points += number / letter_alphabet_possition(word[0])
    else:
        word_points += number * letter_alphabet_possition(word[0])

    if word[-1].isupper():
        word_points -= letter_alphabet_possition(word[-1])
    else:
        word_points += letter_alphabet_possition(word[-1])

    total_sum += word_points

print(f'{total_sum:.2f}')