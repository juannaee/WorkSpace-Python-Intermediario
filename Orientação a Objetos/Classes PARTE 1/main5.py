class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ano = Pessoa.ano_atual - self.idade
        print(f"Ano de nascimento: {ano}")


pessoa_1 = Pessoa("Juan", 21)
pessoa_1.get_ano_nascimento()
