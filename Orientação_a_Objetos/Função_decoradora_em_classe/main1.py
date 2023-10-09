def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name} / {class_dict}"
    return class_repr


def add_my_repr(cls):
    cls.__repr__ = my_repr
    return cls


@add_my_repr
class classTest:
    def __init__(self, nome) -> None:
        self.nome = nome


teste = classTest("Testando")
print(teste)
