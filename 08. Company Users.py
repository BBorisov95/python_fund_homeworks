command = input()

register = {}

while not command == 'End':

    company, employee_id = command.split(' -> ')

    if company not in register:
        register[company] = [employee_id]
    else:
        if employee_id not in register[company]:
            register[company].append(employee_id)

    command = input()

sorted_register = dict(sorted(register.items(), key=lambda x: x))
for company, employee_id in sorted_register.items():
    print(company)
    for e_id in employee_id:
        print(f'-- {e_id}')
