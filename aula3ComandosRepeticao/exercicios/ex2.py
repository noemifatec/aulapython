# A Secretaria de Meio Ambiente, que controla o índice 
# de poluição, mantém três grupos de indústrias que 
# são altamente poluentes do meio ambiente.  A tabela 
# a seguir indica a ação a ser tomada pela Secretaria de 
# Ação 
# acordo com o índice de poluição , leia o índice de 
# poluição:
# Índice de Poluição
# Considerar Aceitável
# Suspender Atividades 
# Grupo1
# Suspender Atividades 
# Grupo  2
# Suspender atividade 
# de todos grupos
# 0  até 2
# 3  até  5
# 6  até 7
# Acima de 8
opcao = int(input ("Digite o índice de poluição"))

match opcao:
    case 0|1|2:
        print("Considerar aceitável")
    case 3|4|5:
        print("Suspender atividades Grupo I")
    case 6|7:
        print("Suspender atividades Grupo II")
    case n if n > 8:
        print("Suspender atividades de todos os Grupos")
    case _:
        print ("Opção inválida")

