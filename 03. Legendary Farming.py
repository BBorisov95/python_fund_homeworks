legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr',
                   'motes': 'Dragonwrath'}


key_items = {'shards': 0, 'fragments': 0, 'motes': 0}

junks = {}

is_found = False
while not is_found:
    data = input().lower().split()

    for index in range(0, len(data), 2):
        material = data[index + 1]
        quantity = int(data[index])
        if material in key_items:
            key_items[material] += quantity
            if key_items[material] >= 250:
                print(f'{legendary_items[material]} obtained!')
                key_items[material] -= 250
                is_found = True
                break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity
    if is_found:
        break

ordered_key_items = {k: v for k, v in sorted(key_items.items(), key=lambda x: (-x[1], x))}

for key_material in ordered_key_items:
    print(f'{key_material}: {ordered_key_items[key_material]}')

ordered_junk = {k: v for k, v in sorted(junks.items(), key=lambda x: x)}
for junk in ordered_junk:
    print(f'{junk}: {ordered_junk[junk]}')