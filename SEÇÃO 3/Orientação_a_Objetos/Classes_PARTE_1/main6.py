class Pessoa:
    ANO_ATUAL = 2023

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def calcular_ano_nascimento(self):
        if self.idade > self.ANO_ATUAL:
            return self.idade - self.ANO_ATUAL
        return self.ANO_ATUAL - self.idade


p1 = Pessoa("Juan", "Guilherme", 21)
print(p1.calcular_ano_nascimento())

p1.__dict__["cpf"] = "10488775400"

print(p1.cpf)
print(vars(p1))
