class Animal:
    def __init__(self, name):
        self.name = name

    def comendo(self, comida):
        return f"{self.name} está comendo {comida}"

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(name="Leão")
print(leao.executar("Maçã"))
