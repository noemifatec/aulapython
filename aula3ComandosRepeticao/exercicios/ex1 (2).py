# Faça um Programa que verifique se 
# uma letra digitada é consoante ou 
# vogal


vogais = ['a','e','i','o','u']
letra = (input(f"Digite uma letra  "))
if letra in vogais:
    print(f"A letra digitada {letra} é vogal")
else:
    print(f"A letra digitada {letra} é consoante")
    