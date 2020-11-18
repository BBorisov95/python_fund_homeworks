n = int(input())

register = {}

def registration(user_name, plate):
    if user_name not in register:
        register[user_name] = plate
        print(f'{user_name} registered {plate} successfully')
    else:
        print(f'ERROR: already registered with plate number {register[user_name]}')
    return register


def unregistration(user_name):
    if user_name not in register:
        print(f'ERROR: user {user_name} not found')
    else:
        print(f'{user_name} unregistered successfully')
        register.pop(user_name)
    return register


for _ in range(n):
    command = input().split()

    if command[0] == 'register':
        register = registration(command[1], command[2])
    elif command[0] == 'unregister':
        register = unregistration(command[1])


for user in register:
    print(f'{user} => {register[user]}')