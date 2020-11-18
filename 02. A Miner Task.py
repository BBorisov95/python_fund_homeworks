word = input()

resources = {}
words = []
while not word == 'stop':
    words.append(word)
    word = input()

for i in range(0, len(words), 2):
    if words[i] not in resources:
        resources[words[i]] = int(words[i+1])
    else:
        resources[words[i]] += int(words[i+1])

for key in resources:
    print(f'{key} -> {resources[key]}')


