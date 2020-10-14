version = [int(num) for num in input().split('.')]

new_version = version.copy()
new_version.reverse()
for index in range(len(new_version)):

    if new_version[index] != 9:
        new_version[index] += 1
    else:
        new_version[index] = 0

    if new_version[index] != 0:
        break
new_version.reverse()

new_version = list(map(str, new_version))

new_version = '.'.join(new_version)

print(new_version)
