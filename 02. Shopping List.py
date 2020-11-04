groceries = input().split('!')

command = input()

while command != 'Go Shopping!':

    tokens = command.split()

    if tokens[0] == 'Urgent':
        if tokens[1] not in groceries:
            groceries.insert(0, tokens[1])
    elif tokens[0] == 'Unnecessary':
        if tokens[1] in groceries:
            groceries.remove(tokens[1])
    elif tokens[0] == 'Correct':
        if tokens[1] in groceries:
            groceries[groceries.index(tokens[1])] = tokens[2]
    elif tokens[0] == 'Rearrange':
        if tokens[1] in groceries:
            groceries.remove(tokens[1])
            groceries.append(tokens[1])

    command = input()

print(', '.join(groceries))