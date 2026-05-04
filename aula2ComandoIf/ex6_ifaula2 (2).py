# RCÍCIOS
# Construa um programa que solicite ao usuário dois números 
# positivos. Em seguida, o programa deve apresentar o seguinte 
# menu.
# 1  Média ponderada, com pesos 2 e 3, respectivamente
# 2. Quadrado da soma dos 2 números 
# 3. Cubo do menor número Escolha uma opção:
# De acordo com a opção informada, o programa deve calcular 
# a operação apresentada no menu. Se a opção escolhida for 
# inválida, o programa deve mostrar a mensagem “Opção 
# inválida” e ser encerrado. 
# Calculo media ponderada: media =(num1 * 2 + num2 * 3) /5
import os
os.system('cls')

print("## Operações ##. \n Digite 1 - Média ponderada \n Digite 2 - Quadrado da soma\n Digite 3 - Cubo do menor número")

num1 = int(input("Digite um número positivo "))
num2 = int(input("Digite outro número positivo "))

if num1 < num2:
    menor = num1
else:
    menor = num2

operacao = int(input("Digite o número da operação"))

match operacao:
    case 1:
        resultado = (num1 * 2 + num2 * 3)/5
    case 2:
        resultado = (num1 + num2) ** 2
    case 3:
        resultado = pow(menor,3)
    case _:
         print("Opção inválida")

print(f"Você escolheu a operação: {operacao} e o resultado é {resultado}")

