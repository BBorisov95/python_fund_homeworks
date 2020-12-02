raw_key = input()


def contains(substring):
    if substring in raw_key:
        print(f'{raw_key} contains {substring}')
    else:
        print('Substring not found!')
    return raw_key


def flip(command, start_ix, end_ix):
    if command == 'Upper':
        upper_key = raw_key[start_ix:end_ix].upper()
        new_raw_key = raw_key[:start_ix] + upper_key + raw_key[end_ix:]
    else:
        lower_key = raw_key[start_ix:end_ix].lower()
        new_raw_key = raw_key[:start_ix] + lower_key + raw_key[end_ix:]
    print(new_raw_key)
    return new_raw_key


def slice(start_ix, end_ix):
    new_key = raw_key[:start_ix] + raw_key[end_ix:]
    print(new_key)
    return new_key

data = input()

while not data == "Generate":

    data = data.split(">>>")

    if data[0] == "Contains":
        raw_key = contains(data[1])
    elif data[0] == "Flip":
        raw_key = flip(data[1], int(data[2]), int(data[3]))
    elif data[0] == "Slice":
        raw_key = slice(int(data[1]), int(data[2]))


    data = input()

print(f'Your activation key is: {raw_key}')