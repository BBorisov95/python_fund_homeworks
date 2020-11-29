import re

data = input()

pattern = r'(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)'

bought = []
total_price = 0

while not data == 'Purchase':

    matches = re.match(pattern, data)
    if matches:
        match = matches.groupdict()
        bought.append(match['name'])
        total_price += float(match['price']) * int(match['quantity'])


    data = input()

print('Bought furniture:')
for product in bought:
    print(product)
print(f'Total money spend: {total_price:.2f}')
