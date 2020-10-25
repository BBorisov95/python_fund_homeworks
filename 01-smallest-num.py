import sys
def smallest_num(number_one, number_two, number_three):
    smallest_number = sys.maxsize
    if number_one < smallest_number:
        smallest_number = number_one
    if number_two < smallest_number:
        smallest_number = number_two
    if number_three < smallest_number:
        smallest_number = number_three
    print(smallest_number)

number_one = int(input())
number_two = int(input())
number_three = int(input())

smallest_num(number_one, number_two, number_three)