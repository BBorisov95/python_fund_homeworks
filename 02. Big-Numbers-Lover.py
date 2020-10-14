numbers = [num for num in input().split()]

numbers.sort(key = str, reverse=True)

numbers = ''.join(numbers)

print(numbers)