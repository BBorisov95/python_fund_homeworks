numbers_as_str = input().split()
numbers_to_remove = int(input())

nums_as_int = [int(n) for n in numbers_as_str]

low_nums = []

for low_number in nums_as_int:
  low_nums.append(low_number)
  
for removes in range(numbers_to_remove):
  to_remove = min(low_nums)
  low_nums.remove(to_remove)
  nums_as_int.remove(to_remove)

print(nums_as_int)
