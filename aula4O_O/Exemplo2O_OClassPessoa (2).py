class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

        #método calcular idade
    def calcularIdade(self):
            anoatual = int(input("Digite ano atual"))
            return anoatual - self.idade 
        
        #instanciar objeto da classe Pessoa
p = Pessoa('Luiz', 25)
print(p.calcularIdade())
pe = Pessoa('Joao', 56)
print(pe.calcularIdade())
        