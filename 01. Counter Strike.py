energy = int(input())

command = input()
counter = 0
while command != 'End of battle':
    if energy < int(command):
        print(f'Not enough energy! Game ends with {counter} won battles and {energy} energy')
        break
    energy -= int(command)
    counter += 1
    if counter % 3 == 0:
        energy += counter

    command = input()

if command == 'End of battle':
    print(f'Won battles: {counter}. Energy left: {energy}')