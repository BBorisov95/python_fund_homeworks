neighborhood = input().split('@')
int_neighborhood = list(map(int, neighborhood))

command = input()

cupid_position = 0

while command != 'Love!':
    
    jump, lenght = command.split()
    lenght = int(lenght)        
    
    for home_index in range(0, len(int_neighborhood)):
        
        cupid_position += lenght
        
        if cupid_position > len(int_neighborhood):
            home_index == 0
        
        if int_neighborhood[home_index] == 0:
            print(f'Place {home_index} already had Valentine\'s day.')
        elif cupid_position <= int_neighborhood[home_index]:
           int_neighborhood[home_index] -= 2
           if int_neighborhood[home_index] == 0:
               print(f'Place {home_index} has Valentine\'s day.')
               
        cupid_position = home_index + 1
            
    
    command = input()
    
print(f'Cupid\'s last position was {cupid_position}.')
fail_homes = 0

for homes in int_neighborhood:
   if homes == 0:
      continue
   elif homes != 0:
       fail_homes += 1
print(f'Cupid has failed {fail_homes} places.')
