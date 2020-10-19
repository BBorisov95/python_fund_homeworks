words = input().split()
list_of_words = []


def digit_to_char(slice):
    char = chr(int(slice))
    return char


def swap_char(word):
    chars_in_word = [char for char in word]
    chars_in_word[1], chars_in_word[-1] = chars_in_word[-1], chars_in_word[1]
    return ''.join(chars_in_word)

for code_word in words:
    if code_word[:3].isdigit():
        word = digit_to_char(code_word[:3]) + code_word[3:]
        right_word = swap_char(word)
        list_of_words.append(right_word)
    elif code_word[:2].isdigit():
        word = digit_to_char(code_word[:2]) + code_word[2:]
        right_word = swap_char(word)
        list_of_words.append(right_word)

print(' '.join(list_of_words))