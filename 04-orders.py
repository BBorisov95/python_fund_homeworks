def orders():
    price = 0
    if product == 'coffee':
        price = 1.5
    elif product == 'coke':
        price = 1.40
    elif product == 'water':
        price = 1.00
    elif product == 'snacks':
        price = 2.00
    result = price * quantity
    print(f'{result:.2f}')

product = input()
quantity = int(input())

orders()