import enum


class TypeProducts(enum.Enum):
    ELETRONIC = enum.auto()
    ORGANIC = enum.auto()
    PLASTIC = enum.auto()


class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._type = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type_products):
        if type_products in TypeProducts:
            self._type = type_products
        print("Tipo de produto não encontrado")

    def describe(self):
        return f"Descrição Produto:\nNome:{self.name}\nPreço:{self.price}\nTipo:{self.type.name if self.type else 'Não definido'}"


produto_1 = Products("Computador", 2500)
produto_1.type = TypeProducts.ELETRONIC
print(produto_1.describe())
