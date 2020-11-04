array = [int(el) for el in input().split()]

commands = input()


def swap(i1, i2):
    i1_value = array[i1]
    i2_value = array[i2]
    array[i1] = i2_value
    array[i2] = i1_value
    return array


def multiply(i1, i2):
    i1_value = array[i1]
    i2_value = array[i2]
    array[i1] = i1_value * i2_value
    return array


def decrease(array):
    return [el -1 for el in array]

while commands != 'end':

    token = commands.split()

    if token[0] == 'swap':
        array = swap(int(token[1]), int(token[2]))
    elif token[0] == 'multiply':
        array = multiply(int(token[1]), int(token[2]))
    elif token[0] == 'decrease':
        array = decrease(array)

    commands = input()

print(", ".join(map(str,array)))