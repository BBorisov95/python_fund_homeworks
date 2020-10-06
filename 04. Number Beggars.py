n = input().split(', ')
beggars = int(input())

numbers = []

for nums in n:
    numbers.append(int(nums))
  
result = [0] * beggars


for beggars_index in range(len(numbers)):
    index = beggars_index % beggars
    result[index] += numbers[beggars_index]

print(result)  
  
                 
