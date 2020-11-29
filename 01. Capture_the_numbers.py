import re

data = input()

matches = []
pattern = r'[0-9]+'
while data:

    match = re.finditer(pattern, data)
    for n in match:
        matches.append(n.group())

    data = input()

for number in matches:
    print(number, end=" ")