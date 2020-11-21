sentence = input()

for el in range(len(sentence)):
    if sentence[el] == ':':
        print(f'{sentence[el] + sentence[el+1] }')