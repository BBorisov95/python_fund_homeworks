string = input().split()

occurence = {}
for word in string:
    for el in word:
        if el in occurence.keys():
            occurence[el] += el
        else:
            occurence[el] = el

for key in occurence:
    print(f'{key} -> {len(occurence[key])}')