import math
p = int(input())
c = int(input())

counts = 0

t = p / c
counts += t


print(math.ceil(counts))
