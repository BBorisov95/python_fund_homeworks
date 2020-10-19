n = [int(el) for el in input().split(', ')]

groups = []
bounder = 10

for group in range(max(n)):
    if len(n) > 0:
        numbers_v = []
        for numbers in n:
            numbers = int(numbers)
            if numbers <= bounder:
                groups.append(numbers)
                numbers_v.append(str(numbers))

        print(f'Group of {bounder}\'s: {groups}')
        for el in numbers_v:
            n.remove(int(el))
        groups.clear()
        bounder += 10
