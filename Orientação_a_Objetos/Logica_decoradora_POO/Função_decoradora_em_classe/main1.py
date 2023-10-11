def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name} / {class_dict}"
    return class_repr


def add_my_repr(cls):
    cls.__repr__ = my_repr
    return cls


def decorator_method(method_):
    def intern(self, *args, **kwargs):
        result = method_(self, *args, **kwargs)
        if "1" in result:
            return "Você escolheu 1"
        return result

    return intern


@add_my_repr
class classTest:
    def __init__(self, name) -> None:
        self.name = name

    @decorator_method
    def test_decorator_method(self):
        return f"Teste: {self.name}"


teste = classTest(1)
print(teste)
print(teste.test_decorator_method())
