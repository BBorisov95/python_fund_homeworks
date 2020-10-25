import math

n = int(input())
y = int(input())

fn = math.factorial(n)
fy = math.factorial(y)

result = fn / fy
print(f'{result:.2f}')