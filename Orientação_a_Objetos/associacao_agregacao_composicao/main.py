class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

        @property
        def ferramenta(self):
            return self._ferramenta

        @ferramenta.setter
        def ferramenta(self, ferramenta):
            self._ferramenta = ferramenta


class ferramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f"{self.nome} está escrevndo...."


escritor_1 = Escritor("Juan")
caneta = ferramentaDeEscrever("Caneta Bic")
escritor_1.ferramenta = caneta
print(escritor_1.ferramenta.escrever())
