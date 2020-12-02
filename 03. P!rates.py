

command = input()

places = {}

while not command == "Sail":

    city, population, gold = command.split('||')
    population = int(population)
    gold = int(gold)
    if city in places:
        places[city]['population'] += population
        places[city]['gold'] += gold
    else:
        places[city] = {'population': population, 'gold': gold}

    command = input()

command = input()

while not command == "End":
    command = command.split('=>')
    if command[0] == "Plunder":
        places[command[1]]['population'] -= int(command[2])
        places[command[1]]['gold'] -= int(command[3])
        print(f'{command[1]} plundered! {command[3]} gold stolen, {command[2]} citizens killed.')
        if places[command[1]]['gold'] == 0 or places[command[1]]['population'] == 0:
            print(f'{command[1]} has been wiped off the map!')
            del places[command[1]]
    elif command[0] == "Prosper":
        if int(command[2]) < 0:
            print('Gold added cannot be a negative number!')
            command = input()
            continue
        else:
            places[command[1]]['gold'] += int(command[2])
            print(f'{command[2]} gold added to the city treasury. {command[1]} now has {places[command[1]]["gold"]} gold.')


    command = input()


print(f'Ahoy, Captain! There are {len(places)} wealthy settlements to go to:')

if len(places) == 0:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    ordered_places = dict(sorted(places.items(), key=lambda x: (-x[1]['gold'], x)))
    for town in ordered_places:
        print(f'{town} -> Population: {ordered_places[town]["population"]} citizens, Gold: {ordered_places[town]["gold"]} kg')
