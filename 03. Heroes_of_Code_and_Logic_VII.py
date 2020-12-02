num_of_heroes = int(input())

heroes = {}


def cast_spell(hero, mp, spell_name):
    if heroes[hero]['hero_mp'] >= mp:
        heroes[hero]['hero_mp'] -= mp
        print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero]["hero_mp"]} MP!')
    else:
        print(f'{hero} does not have enough MP to cast {spell_name}!')
    return heroes


def take_damage(hero, dmg, attacker):
    if heroes[hero]['hero_hp'] > dmg:
        heroes[hero]['hero_hp'] -= dmg
        if heroes[hero]['hero_hp'] >= 0:
            print(f'{hero} was hit for {dmg} HP by {attacker} and now has {heroes[hero]["hero_hp"]} HP left!')
    else:
        print(f'{hero} has been killed by {attacker}!')
        del heroes[hero]
    return heroes


def recharge(hero, mp):

    if heroes[hero]['hero_mp'] + mp >= 200:
        recovery_amount = 200 - heroes[hero]['hero_mp']
        heroes[hero]['hero_mp'] = 200
        print(f"{hero} recharged for {recovery_amount} MP!")
    else:
        heroes[hero]['hero_mp'] += mp
        print(f'{hero} recharged for {mp} MP!')
    return heroes


def heal(hero, hp):

    if heroes[hero]['hero_hp'] + hp >= 100:
        recovery_amount = 100 - heroes[hero]['hero_hp']
        heroes[hero]['hero_hp'] = 100
        print(f'{hero} healed for {recovery_amount} HP!')
    else:
        heroes[hero]['hero_hp'] += hp
        print(f'{hero} healed for {hp} HP!')
    return heroes


for _ in range(num_of_heroes):
    hero_name, hero_hp, hero_mp = input().split()

    heroes[hero_name] = {'hero_hp': int(hero_hp), 'hero_mp': int(hero_mp)}

commands = input()

while not commands == 'End':
    commands = commands.split(' - ')

    if commands[0] == 'CastSpell':
        heroes = cast_spell(commands[1], int(commands[2]), commands[3])
    elif commands[0] == 'TakeDamage':
        heroes = take_damage(commands[1], int(commands[2]), commands[3])
    elif commands[0] == 'Recharge':
        heroes = recharge(commands[1], int(commands[2]))
    elif commands[0] == 'Heal':
        heroes = heal(commands[1], int(commands[2]))

    commands = input()

ordered_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]['hero_hp'], x)))

for hero in ordered_heroes:
    print(hero)
    print(f'  HP: {ordered_heroes[hero]["hero_hp"]}')
    print(f'  MP: {ordered_heroes[hero]["hero_mp"]}')
