class Carro:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def run(self):
        print(f"{self.name}, está acelerando")


carro_1 = Carro(name="Ford", value=25000)
carro_1.run()

