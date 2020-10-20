neighborhood = input().split('@')
int_neighborhood = list(map(int, neighborhood))

command = input()

cupid_position = None

while command != 'Love!':
    
    action, lenght = command.split()
            
    
    for home_index in range(0, int_neighborhood, lenght):
        
        if lenght > len(int_neighborhood):
            home_index == 0
        
        if int_neighborhood[home_index] == 0:
            print(f'Place {home_index} already had Valentine\'s day.')
        elif lenght <= int_neighborhood[home_index]:
           int_neighborhood[home_index] -= 2
           if int_neighborhood[home_index] == 0:
               print(f'Place {home_index} has Valentine\'s day.')
               
        cupid_position = home_index
            
    
    command = input()
    
print(f'Cupid\'s last position was {cupid_position}')
for homes in int_neighborhood:
   fail_homes = 0
   if homes == 0:
      continue
   elif homes != 0:
       fail_homes += 1
       print(f'Cupid has failed {fail_homes} places.')
