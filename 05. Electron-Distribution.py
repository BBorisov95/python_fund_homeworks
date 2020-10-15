import math
electrons = int(input())

electron_in_shells = [shell for shell in range(1, electrons +1) if math.ceil((2 * electrons **2) / 100)) ]

while sum(electron_in_shells != electrons

  for electron in range(electrons):
    for shell_index in electron_in_shells:
      max_num_in_shell = 2 * shell_index**2
      if electron_in_shells[shell_index] < max_num_in_shell
         electron_in_shells[shell_index].append(electron)
  
#•	Maximum number of electrons in a shell is distributed with a rule of 2n^2 (n being position of a shell a.k.a. the list index + 1).
#•	For example, maximum number of electrons in 3rd shield is 2*3^2 = 18.
#•	Electrons should fill the lowest level shell first.
#•	If the electrons have completely filled the lowest level shell, the other unoccupied electrons will fill the higher level shell and so on.
