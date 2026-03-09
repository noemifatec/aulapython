# Leia a altura de 3 pessoas. Ao fim, o 
# programa deve mostrar as estaturas em 
# ordem decrescente. Mostrar a pessoa de 
# maior altura , altura mediana , e menor 
# altura

import os
os.system('cls')

alt1 = float(input("Digite a altura 1 "))
alt2 = float(input("Digite a altura 2 "))
alt3 = float(input("Digite a altura 3 "))

if alt1 > alt2 > alt3:
    maior = alt1
    if alt2 > alt3:
     mediana = alt2
     menor = alt3
    else:
       mediana = alt3
       menor = alt2

if alt2>alt1>alt3:
   maior = alt2
   if alt1 > alt3:
      mediana = alt1
      menor = alt3
   else:
      mediana = alt3
      menor = alt1

if alt3 > alt1 > alt2:
   maior = alt3
   if alt1 > alt3:
      mediana = alt1
      menor = alt3
   else:
      mediana = alt3
      menor = alt1
print(f"A pessoa maior tem: {maior} metros, a mediana tem {mediana} metros e a menor tem {menor} metros")


