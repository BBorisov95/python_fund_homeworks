n = [int(el) for el in input().split()]

average_n = sum(n) / len(n)

bigger_then_average = [el for el in n if el > average_n]
bigger_then_average.sort(reverse=True)

if len(bigger_then_average) < 1:
    print('No')
else:
    print(" ".join(map(str,bigger_then_average[:5])))