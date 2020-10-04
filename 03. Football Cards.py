card = input().split(' ')

terminated = False
team_a = []
for players in range(1, 11 + 1):
    players_name = f'A-{players}'
    team_a.append(players_name)
team_b = []
for players in range(1, 11 + 1):
    players_name = f'B-{players}'
    team_b.append(players_name)

for cards in card:
    if cards in team_a:
        team_a.remove(cards)
    elif cards in team_b:
        team_b.remove(cards)
    else:
        continue

    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

if terminated:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
    print(f'Game was terminated')
else:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
