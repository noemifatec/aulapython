nulos = int(input("Digite qtde votos nulos"))
brancos = int(input("Digite qtde votos brancos"))
validos = int(input("Digite qtde votos válidos"))

num_total_eleitores = nulos + brancos + validos

Percbrancos = (brancos * 100)/num_total_eleitores
Percnulos = (nulos * 100)/num_total_eleitores
Percvalidos = (validos * 100)/num_total_eleitores

print(f"Porcentagem de brancos: {Percbrancos}")
print(f"Porcentagem de nulos: {Percnulos}")
print(f"Porcentagem de válidos: {Percvalidos}")