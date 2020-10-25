import sys

array = input().split()
exchanged_array = array

while True:

    command = input().split(' ')
    if command[0] == 'end':
        break
    task = command[0]
    task_one = command[1]
    if len(command) > 2:
       task_two = command[2]


    if task == 'exchange':
        #  splits the array after the given index, and exchanges the places of the two resulting sub-arrays.
        #  E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
        exchanged_array = exchanged_array[int(task_one) + 1::] + exchanged_array[:int(task_one) + 1]
        if int(task_one) > len(array):
            print('Invalid index')
            continue
    elif task == 'max':
        if task_one == 'even':
            max_even_index = 0
            max_even = 0
            for i in range(len(exchanged_array)):
                if int(exchanged_array[i]) >= max_even:
                    max_even = int(exchanged_array[i])
                    max_even_index = i
                if max_even == 0:
                    print('No matches')
            print(max_even_index)
        else:
            max_odd_index = 0
            max_odd = 0
            for i in range(len(exchanged_array)):
                if int(exchanged_array[i]) >= max_odd:
                    max_odd = int(exchanged_array[i])
                    max_odd_index = i
                if max_odd == 0:
                    print('No matches')
            print(max_odd_index)
    elif task == 'min':
        if task_one == 'even':
            min_even_index = 0
            min_even = sys.maxsize
            for i in range(len(exchanged_array)):
                if int(exchanged_array[i]) <= min_even and int(exchanged_array[i]) % 2 == 0:
                    min_even = int(exchanged_array[i])
                    min_even_index = i
            if min_even == sys.maxsize:
                print('No matches')
                continue
            print(min_even_index)
        else:
            min_odd_index = 0
            min_odd = sys.maxsize
            for i in range(len(exchanged_array)):
                if int(exchanged_array[i]) <= min_odd:
                    min_odd = int(exchanged_array[i])
                    min_odd_index = i
            if min_odd == 0:
                print('No matches')
            print(min_odd_index)

    elif task == 'first':

        searched_count = int(task_one)
        if searched_count > len(exchanged_array):
            print('Invalid count')
            continue

        if task_two == 'even':
            first_even = []
            for num in exchanged_array:
                if int(num) % 2 == 0:
                    first_even.append(num)
                if searched_count == len(first_even):
                    print(first_even)
                    break
            print(first_even)
        else:
            first_odd = []
            for num in exchanged_array:
                if int(num) % 2 != 0:
                    first_odd.append(num)
                if searched_count == len(first_odd):
                    print(first_odd)
                    break
            print(first_odd)
    elif task == 'last':
        searched_count = int(task_one)
        if searched_count > len(exchanged_array):
            print('Invalid count')

        if task_two == 'even':
            last_even = []
            for num in exchanged_array[::-1]:
                if int(num) % 2 == 0:
                    last_even.append(num)
                if searched_count == len(last_even):
                    print(last_even[::-1])
                    break
            print(last_even)
        else:
            last_odd = []
            for num in exchanged_array[::-1]:
                if int(num) % 2 != 0:
                    last_odd.append(num)
                if searched_count == len(last_odd):
                    print(last_odd[::-1])
                    break
            print(last_odd)


print(exchanged_array)

### TODO да оправя принтовете да не са стрингове