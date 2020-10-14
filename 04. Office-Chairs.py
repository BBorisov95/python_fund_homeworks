rooms = int(input())

free_chairs = 0

for room in range(rooms):
    chair, taken_chair = input().split(' ')
    taken_chair = int(taken_chair)

    if len(chair) >= taken_chair:
        free_chairs += len(chair) - taken_chair
    elif len(chair) <= taken_chair:
        needed_chairs = abs(taken_chair - len(chair))
        print(f'{needed_chairs} more chairs needed in room {room}')
    else:
        print(f'Game on, {free_chairs} free chairs left')