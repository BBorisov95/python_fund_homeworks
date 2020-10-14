first_list = [word for word in input().split(', ')]
second_list = [word for word in input().split(', ')]

result = []

for el in first_list:
    for word in second_list:
        if el in word:
            if el not in result:
                result.append(el)

print(result)

