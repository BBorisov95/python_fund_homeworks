cards = input().split()
n_of_shuffles = int(input())

half = len(cards) // 2


for suffle in range(n_of_shuffles):
  current_shuffle = zip(cards[:half], cards[half:])

  cards.clear()
  for pair in current_shuffle:
    cards.extend(pair)


print(cards)
