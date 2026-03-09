opc = int(input("\n 1-Sacar \n 2-Extrato \3 -Sair\n Escolha a aopão:  "))

match opc:
    case 1:
        print("Você escolheu a opção sacar " )
              valor = float(input("Digite o valor do saque"))
              print(f"Sacando da sua conta ... o valor de R$  {valor}")
     case 2:
          print("Você escolheu a opção extrato")
          dias        