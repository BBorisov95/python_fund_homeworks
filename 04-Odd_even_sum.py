n = input()

odd_sum = 0
even_sum = 0

for i in n:

    if int(i) % 2 != 0:
        odd_sum += int(i)
    else:
        even_sum += int(i)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}" )
