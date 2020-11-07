from math import floor
workers_biscuit_per_day = int(input())
workers = int(input())
other_company_biscuit = int(input())

total_biscuit_per_day = workers_biscuit_per_day * workers
total_biscuit = 0
for day in range(1, 31):

    if day % 3 == 0:
        total_biscuit += floor(total_biscuit_per_day * 0.75)
    else:
        total_biscuit += floor(total_biscuit_per_day)

print(f'You have produced {int(total_biscuit)} biscuits for the past month.')
diff_in_pc = total_biscuit - other_company_biscuit
diff_in_per = abs(diff_in_pc / other_company_biscuit * 100)

if total_biscuit > other_company_biscuit:
    print(f'You produce {diff_in_per:.2f} percent more biscuits.')
else:
    print(f'You produce {diff_in_per:.2f} percent less biscuits.')
