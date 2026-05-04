import os
os.system('cls')

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

peso1 =float(input("Digite o primeiro peso"))
peso2 =float(input("Digite o segundo peso "))

if peso1 > peso2:
    print(f"A pessoa {nome1} è mais pesada,com {peso1} kilos")
elif peso2 > peso1:
    print(f"A pessoa {nome2} é mais pesada, com {peso2} kilos")
else:
    print(f"As pessoas tem o mesmo peso: {peso1} kilos")
