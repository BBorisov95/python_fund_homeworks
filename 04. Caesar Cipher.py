line = input()

new_word = ''

for el in line:
    new_word += chr(ord(el) + 3)

print(new_word)