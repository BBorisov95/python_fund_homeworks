user_name = input()

command = input()


def case(u_n, specific):
    new_user_name = ''
    if specific == 'lower':
        new_user_name = u_n.lower()
    elif specific == 'upper':
        new_user_name = u_n.upper()

    print(new_user_name)

    return new_user_name


def reverse_name(u_n, start_indx, end_indx):
    if start_indx in range(len(u_n)) and end_indx in range(len(u_n)):
        reversed_substring = u_n[start_indx : end_indx + 1]
        print(reversed_substring[::-1])


def cutted(sub_string):
    #to check if we have more then 1 sub string
    cutted_name = ''
    if sub_string in user_name:
        cutted_name = user_name.replace(sub_string, '')
    else:
        print(f'The word {user_name} doesn\'t contain {sub_string}.')
    print(cutted_name)
    return cutted_name


def replaced(char):
    replaced_char = user_name.replace(char, '*')
    print(replaced_char)
    return replaced_char


def checked(char):
    if char in user_name:
        print('Valid')
    else:
        print(f'Your username must contain {char}.')


while not command == 'Sign up':

    command = command.split()


    if command[0] == 'Case':
        user_name = case(user_name, command[1])
    elif command[0] == 'Reverse':
        reverse_name(user_name, int(command[1]), int(command[2]))
    elif command[0] == 'Cut':
        user_name = cutted(command[1])
    elif command[0] == 'Replace':
        user_name = replaced(command[1])
    elif command[0] == 'Check':
        checked(command[1])

    command = input()