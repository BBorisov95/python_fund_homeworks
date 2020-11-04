targets = [int(el) for el in input().split()]

command = input()
shoot_targets = 0

while command != 'End':

    index = int(command)

    if index in range(len(targets)):
        current_index_value = targets[index]
        targets[index] = -1
        for el in targets:
            if el > current_index_value and current_index_value != -1:
                targets[targets.index(el)] = el - current_index_value
            elif 0 < el <= current_index_value:
                targets[targets.index(el)] = el + current_index_value
            print(f'the index of {el} is {targets[targets.index(targets[index])]}')
        if current_index_value != -1:
            shoot_targets += 1
    targets = [int(el) for el in input().split()]

    command = input()

    while command != 'End':
        count = -1
        index = int(command)
        if index in range(len(targets)):
            current_index_value = targets[index]
            targets[index] = -1
            for el in targets:
                count += 1
                if el > current_index_value and not current_index_value == -1:
                    targets[count] = el - current_index_value
                else:
                    if not el == -1:
                        targets[count] = el + current_index_value

        command = input()

    print(f'Shot targets: {len([_ for _ in targets if _ == -1])} -> {" ".join(list(map(str, targets)))}')

    command = input()

print(f'Shot targets: {shoot_targets} -> {" ".join(map(str,targets))}')