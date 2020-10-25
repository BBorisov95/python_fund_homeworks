char_one = input()
char_two = input()

for i in range (ord(char_one) + 1, ord(char_two)):
    print(chr(i), end=" ")