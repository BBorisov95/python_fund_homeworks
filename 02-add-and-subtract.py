def add_number(a, b):
    result = a + b
    return result


a = int(input())
b = int(input())
c = int(input())

sum = add_number(a, b)
res = sum - c
print(res)