from abc import ABC, abstractmethod


class Abastrato_teste(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def teste_enviar(self) -> bool:
        ...

    @abstractmethod
    def teste_enviar_2(self, msg) -> str:
        ...


class Abastrato_teste_2(Abastrato_teste):
    def __init__(self) -> None:
        super().__init__()

    def teste_enviar(self) -> bool:
        return True

    def teste_enviar_2(self, msg) -> str:
        return msg


def testando(teste: Abastrato_teste):
    if teste.teste_enviar():
        print("Deu true")
    else:
        print("Deu false")


def testando_2(teste: Abastrato_teste, msg):
    print(teste.teste_enviar_2(msg))


teste = Abastrato_teste_2()
testando(teste)
teste_2 = Abastrato_teste_2()
testando_2(teste_2, "testetete")
