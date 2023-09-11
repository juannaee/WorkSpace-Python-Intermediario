class Camara:
    def __init__(self, name, filmando=False):
        self.name = name
        self.filmando = filmando

    def filmar(self):
        if self.estar_filmando():
            return
        print(f"{self.name} está filmando")
        self.filmando = True

    def estar_filmando(self):
        if self.filmando:
            print(f"{self.name} já esta filmando")
            return True
        return False

    def desligar_filmando(self):
        if self.estar_filmando():
            print(f"Desligando filmagem da camera {self.name}")
            self.filmando = False
            return
        print(f"A camera{self.name} não está com filmagem ativa!!")


c1 = Camara("Sony")
c2 = Camara("Multivideo")

c1.desligar_filmando()
c1.filmar()
c1.filmar()
c1.desligar_filmando()
