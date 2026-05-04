opcao = int(input("Digite \n -1 para tensão \n -2 para resistência \n -3 para corrente"))

match opcao:
    case 1:
        R=float(input("Digite resistência "))
        i=float(input("Digite a corrente "))
        print(f"A tensão é {R*i} volts")
    case 2:
        U=float(input("Digite a tensão "))
        i=float(input("Digite a corrente "))
        print(f"A resistência é {U/i} Ohm")
    case 3:
         U=float(input("Digite a tensão "))
         R=float(input("Digite resistência "))
         print(f"A corrente é {U/R} ampère")
    case _ :
        print("Opção inválida")



