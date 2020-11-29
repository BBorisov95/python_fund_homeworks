import re

line = input()

pattern = r'\b(_{1}[a-zA-Z]+\b)'

matches = [x[1:] for x in re.findall(pattern, line)]

print(','.join(matches))