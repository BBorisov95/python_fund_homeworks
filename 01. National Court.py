employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
total_people = int(input())

hours = 0
while total_people > 0:

    total_people -= employee_1 + employee_2 + employee_3
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f'Time needed: {hours}h.')
