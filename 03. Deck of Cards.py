collection = input().split(', ')
number = int(input())

def add(item):
    if item in collection:
        print('Card is already bought')
    else:
        print('Card successfully bought')
        collection.append(tokens[1])

while number > 0:
    command = input()
    tokens = command.split(', ')

    if tokens[0] == 'Add':
        add(tokens[1])
    elif tokens[0] == 'Remove':
        if tokens[1] in collection:
            print('Card successfully sold')
            collection.remove(tokens[1])
        else:
            print('Card not found')
    elif tokens[0] == 'Remove At':
        if int(tokens[1]) in range(len(collection)):
            collection.pop(int(tokens[1]))
            print('Card successfully sold')
        else:
            print('Index out of range')
    elif tokens[0] == 'Insert':
        if int(tokens[1]) > len(collection):
            print('Index out of range')
        else:
            if tokens[2] not in collection:
                print('Card successfully bought')
                collection.insert(int(tokens[1]), tokens[2])
            else:
                print('Card is already bought')

    number -= 1

print(', '.join(collection))

