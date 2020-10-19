targets = [int(num) for num in input().split()]

command = input()


def shoot(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add_target(targets, index, power):
    if 0 <= index < len(targets):
        targets.insert(index, power)
    else:
        print('Invalid placement!')
    return targets


def strike(targets, index, radius):
    left_side = index - radius
    right_side = index + radius

    if left_side >= 0 and right_side < len(targets):
        left_part = targets[:left_side]
        right_part = targets[right_side + 1:]
        targets = left_part + right_part
    else:
        print('Strike missed!')
    return targets


while command != 'End':
    action, index, power = command.split()
    index = int(index)
    power = int(power)

    if action == 'Shoot':
        targets = shoot(targets,index,power)
    elif action == 'Add':
        targets = add_target(targets,index,power)
    elif action == 'Strike':
        targets = strike(targets, index, power)

    command = input()

print('|'.join(map(str,targets)))
