import re

n = int(input())

pattern = r'^(\$|\%)(?P<tag>[A-Z][a-z]{2,})\1\:[ ](?P<digits>(\[[0-9]{2,}\]\|){3})$'

for _ in range(n):
    message = input()

    matches = re.match(pattern, message)
    if not matches:
        print('Valid message not found!')
    else:
        matches.groupdict()
        digits = re.findall(r"\d{2,3}", matches['digits'])
        decrypted_msg = ''
        for el in digits:
            decrypted_msg += chr(int(el))
        print(f'{matches["tag"]}: {decrypted_msg}')
