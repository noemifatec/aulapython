#Exemplo for utilizando lista de valores pré-definidos

frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for lista in frutas:
    print(lista)


    # buscar = 'goiaba'
    # frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
    # for lista in frutas:
    #     if item in frutas == buscar:
    #         print(f"Fruta encontrada {buscar}")
    #         break
    #     else:
    #         print(f"Fruta não encontrada {buscar}")
    buscar = 'goiaba'
frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']

for item in frutas: # Mudei o nome para 'item' para ficar mais claro
    if item == buscar: # Aqui comparamos a fruta da vez com a busca
        print(f"Fruta encontrada: {buscar}")
        break
    else:
        print(f"Ainda procurando... {item} não é {buscar}")