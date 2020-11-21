line = input().split('\\')

print(f'File name: {line[-1].split(".")[0]}')
print(f'File extension: {line[-1].split(".")[1]}')
