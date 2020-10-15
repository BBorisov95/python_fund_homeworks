rooms = int(input())

free_chairs = 0
is_valid = True
  
for room in range(1, rooms + 1):
    chair, taken_chair = input().split(' ')
    taken_chair = int(taken_chair)

    if len(chair) >= taken_chair:
        free_chairs += len(chair) - taken_chair
    else:
      is_valid = False
      needed_chairs = abs(taken_chair - len(chair)) 
      print(f'{needed_chairs} more chairs needed in room {room}')
        

if is_valid:
   print(f'Game On, {free_chairs} free chairs left')
