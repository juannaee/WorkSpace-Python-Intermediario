class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Metodo de instancia:
    def apresentacao(self):
        print(f"Dados:\nNome: {self.nome}\nIdade: {self.idade}")

    def criar_usuario_anonimo(self, idade):
        self.idade = idade
        self.nome = "Anonimo"

    # Metodo de classe:
    @classmethod
    def usuario_anonimo(cls, idade):
        return cls("Anonimo", idade)


print("--------------------------------")
p1 = Pessoa("Juan", 22)
p1.apresentacao()
print("--------------------------------")
p2 = Pessoa()
p2.criar_usuario_anonimo(30)
p2.apresentacao()
print("--------------------------------")
p3 = Pessoa.usuario_anonimo(25)
p3.apresentacao()
print("--------------------------------")
