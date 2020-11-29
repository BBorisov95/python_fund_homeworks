import re

txt = input()

pattern = r'(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+'
#match = []
result = re.finditer(pattern, txt)

for el in result:
    print(el.group())