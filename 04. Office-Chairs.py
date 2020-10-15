rooms = int(input())

free_chairs = 0

for room in range(1, rooms + 1):
    chair, taken_chair = input().split(' ')
    taken_chair = int(taken_chair)

    if len(chair) >= taken_chair:
        free_chairs += len(chair) - taken_chair
    else:
        needed_chairs = abs(taken_chair - len(chair))
        print(f'{needed_chairs} more chairs needed in room {room}')
        free_chairs = 0

if free_chairs > 0:
  print(f'Game On, {free_chairs} free chairs left')
