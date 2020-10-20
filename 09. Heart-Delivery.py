neighborhood = input().split('@')
int_neighborhood = list(map(int, neighborhood))

command = input()

cupid_position = 0
cr = 0
while command != 'Love!':
    
    jump, lenght = command.split()
    lenght = int(lenght)

    #for home_index in range(0, len(int_neighborhood)):

    cupid_position = cr + lenght
        
    if cupid_position >= len(int_neighborhood):
       cupid_position = 0
        
    if int_neighborhood[cupid_position] == 0:
        print(f'Place {cupid_position} already had Valentine\'s day.')
    else:

        int_neighborhood[cupid_position] -= 2
        if int_neighborhood[cupid_position] == 0:
           print(f'Place {cupid_position} has Valentine\'s day.')

    cr = cupid_position

            
    
    command = input()
    
print(f'Cupid\'s last position was {cupid_position}.')
fail_homes = 0

for homes in int_neighborhood:
   if homes == 0:
      continue
   elif homes != 0:
       fail_homes += 1
print(f'Cupid has failed {fail_homes} places.')
