hp = 100
bitcoin = 0


rooms = input().split('|')

while hp > 0:

    for room in rooms:
        command, number = room.split()
        number = int(number)
        if command == 'potion':
            if hp + number >= 100:
                heal = 100 - hp
                print(f'You healed for {heal} hp.')
                hp = 100
            else:
                hp += number
                print(f'You healed for {number} hp.')
            print(f'Current health: {hp} hp.')

        elif command == 'chest':
            bitcoin += number
            print(f'You found {number} bitcoins.')
        else:
            hp -= number
            if hp > 0:
                print(f'You slayed {command}.')
            else:
                print(f'You died! Killed by {command}.')
                print(f'Best room: {rooms.index(room) + 1}')
                break
    if hp > 0:
        print(f'You\'ve made it!')
        print(f'Bitcoins: {bitcoin}')
        print(f'Health: {hp}')
        break

