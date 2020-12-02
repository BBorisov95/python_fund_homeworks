import re

line = input()

emoji_pattern = r'((\:{2}|\*{2})[A-Z][a-z]{2,}\2)'
numbers_pattern = r'\d'

emoji_count = re.findall(emoji_pattern, line)
numbers_in_text = [int(x) for x in re.findall(numbers_pattern, line) if x.isdigit()]

threshold = 1
for num in numbers_in_text:
    threshold *= num

print(f'Cool threshold: {threshold}')

print(f'{len(emoji_count)} emojis found in the text. The cool ones are:')

cool_emoji = {}

for emoji in emoji_count:
    coolnes = 0
    for char in emoji[0]:
        if char.isalpha():
            coolnes += ord(char)
    cool_emoji[emoji[0]] = coolnes

for emoji in cool_emoji:
    if cool_emoji[emoji] >= threshold:
        print(emoji)