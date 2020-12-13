emails = {}

command = input()

while not command == 'Statistics':
    command = command.split('->')

    if command[0] == 'Add':
        if command[1] in emails:
            print(f'{command[1]} is already registered')
        else:
            emails[command[1]] = []
    elif command[0] == 'Send':
        emails[command[1]].append(command[2])
    elif command[0] == 'Delete':
        if command[1] in emails:
            del emails[command[1]]
        else:
            print(f'{command[1]} not found!')

    command = input()

print(f"Users count: {len(emails)}")

ordered_emails = dict(sorted(emails.items(), key=lambda x: (-len(x[1]), x[0])))

for user, value in ordered_emails.items():
    print(user)
    for email in value:
        print(f' - {email}')