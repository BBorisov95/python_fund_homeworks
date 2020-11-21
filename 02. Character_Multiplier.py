words = input().split()

result = 0

if len(words[0]) == len(words[1]):

    for char in range(len(words[0])):
       result += ord(words[0][char]) * ord(words[1][char])

else:
    short_word = ''
    longer_word = ''
    if len(words[0]) < len(words[1]):
        short_word = words[0]
        longer_word = words[1]
    else:
        short_word = words[1]
        longer_word = words[0]
    temp_result = 0
    for char in range(len(short_word)):
        temp_result += ord(short_word[char]) * ord(longer_word[char])

    longer_word = longer_word[len(short_word):]
    for char in range(len(longer_word)):
        temp_result += ord(longer_word[char])
    result = temp_result

print(result)