class Pessoa:
    def __init__(self, name):
        self.name = name

    def get_name_2(self):
        return self.name

    @property
    def get_name(self):
        return self.name


p1 = Pessoa("Juan")
print(p1.get_name_2())
print(p1.get_name)
