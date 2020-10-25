def loading_bar(n):

    for percent in range(n):
        if percent == 0:
            print('[', end='')
        print('%', end='')

    for dots in range(10 - n):
        print('.', end='')
    print(']', end='')


n = (int(input()) // 10)

if n == 10 :
    print(f"{n * 10}% Complete!")
    loading_bar(n)
else:
    print(f"{n * 10}% ", end='')
    loading_bar(n)
    print()
    print("Still loading...")