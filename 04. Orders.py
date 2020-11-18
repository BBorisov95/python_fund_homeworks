products = {}

command = input()

while not command == 'buy':

    product, price, quantity = command.split()

    if product not in products:
        products[product] = {'price': float(price), 'quantity': int(quantity)}
    else:
        products[product]['price'] = float(price)
        products[product]['quantity'] += int(quantity)

    command = input()


for el in products:
    total_price = products[el]['price'] * products[el]['quantity']
    print(f'{el} -> {total_price:.2f}')