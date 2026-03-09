salario = float(input("Digite o salario atual"))
porc_aumento = float(input("Digite a procentagem de aumento"))
novo_salario = (salario + salario * porc_aumento/100)
print(f"O novo salário é R$ {novo_salario:.2f}")