factor = int(input())
count = int(input())

res = []

for x in range(1, count + 1):
    mult = factor * x
    res.append((mult))

print(res)
