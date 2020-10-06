cards = input().split()
n_of_shuffles = int(input())

half = len(cards) // 2

first_card = cards[0]
last_card = cards[-1]

left_side = cards[1:half]
right_side = cards[half:-1]


final_deck = []
print(final_deck)
