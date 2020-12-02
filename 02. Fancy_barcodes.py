import re

num_of_lines = int(input())

pattern = r'@\#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@\#+'

for _ in range(num_of_lines):
    barcode = input()

    if re.match(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
