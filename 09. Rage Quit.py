data = input()

rage_str = ''
letters = []
for i in range(len(data)):
    if not data[i].isdigit():
        letters.append(data[i])
    else:
        number = []
        for char in (data[i:]):
            if char.isdigit():
                number.append(char)
            else:
                break
        number = ''.join(number)
        rage_str += (''.join(letters) * int(number)).upper()
        letters.clear()


print(f'Unique symbols used: {len(set(rage_str))}')
print(rage_str)
