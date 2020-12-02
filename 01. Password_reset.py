starting_str = input()

line = input()


def take_odd(password):
    odd_chars = ''
    for indx, char in enumerate(password):
        if not indx % 2 == 0:
            odd_chars += char
    print(odd_chars)
    return odd_chars


def cut(password, idx, length):

    cutted = password[:idx] + password[idx + length:]

    print(cutted)
    return cutted


def substitute(sub_str, subst):

    if sub_str in starting_str:
        substituted_str = starting_str.replace(sub_str, subst)
        print(substituted_str)
        return substituted_str
    else:
        print('Nothing to replace!')
        return starting_str

while not line == 'Done':
    command = line.split()

    if command[0] == 'TakeOdd':
        starting_str = take_odd(starting_str)
    elif command[0] == 'Cut':
        starting_str = cut(starting_str, int(command[1]), int(command[2]))
    elif command[0] == 'Substitute':
        starting_str = substitute(command[1], command[2])

    line = input()

print(f'Your password is: {starting_str}')
