duma_edno = input()
duma_dve = input()

for a in range(len(duma_edno)):
  if duma_edno[a] != duma_dve[a]:
    for duma_dve_index in range(0, a + 1):
      print(duma_dve[duma_dve_index], end='')

    for duma_edno_index in range(a + 1 , len(duma_edno)):
      print(duma_edno[duma_edno_index], end='')

    print()
