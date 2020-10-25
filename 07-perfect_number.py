def is_perfect(n):
    divisors = 0

    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors += i
        else:
            continue

    if n == divisors:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


n = int(input())
is_perfect(n)

