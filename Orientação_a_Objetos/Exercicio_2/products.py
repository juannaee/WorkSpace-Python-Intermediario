from abc import ABC, abstractmethod
from util import Order_number, Sale_id


class Product(ABC):
    def __init__(self):
        self.products = []
        self.order_number = Order_number.generate_order_number()
        self.sale_id = Sale_id.generate_id_number()

    @abstractmethod
    def calc_price(self):
        raise NotImplementedError("Você deve escolher uma classe produto especifica!")

    @abstractmethod
    def add_product(self):
        raise NotImplementedError("Você deve escolher uma classe produto especifica!")

    @abstractmethod
    def extract_product(self):
        raise NotImplementedError("Você deve instanciar uma classe produto especifica!")


class Long_band(Product):
    def __init__(self):
        super().__init__()
        self.product_options = {
            1: {
                "Nome": "300 MB",
                "Preço": 149.99,
                "Pontos": 250,
            },
            2: {
                "Nome": "200 MB",
                "Preço": 99.99,
                "Pontos": 100,
            },
            3: {
                "Nome": "600 MB",
                "Preço": 199.99,
                "Pontos": 500,
            },
        }

    def calc_price(self):
        return super().calc_price()

    def add_product(self):
        print("Escolha um produto: ")
        while True:
            for options, product_info in self.product_options.items():
                print(f"{options}:{product_info['Nome']}")
            try:
                option_bls = int(input())
                if option_bls not in self.product_options:
                    print("Opção inválida. Escolha uma opção válida.")
                    continue
                self.products.append(self.product_options[option_bls])
                print("Produto adicionado com sucesso !")
            except ValueError:
                print("Você deve digitar um valor numero!")
            another_product = input("Deseja adicionar mais produtos? (S/N): ").lower()
            if another_product != "s":
                break

    def extract_product(self):
        print("###############################")
        print(f"ID VENDA: {self.sale_id}\nNUMERO DA ORDEM:{self.order_number}")
        for product_info in self.products:
            print("###############################")
            print(
                f"Nome: {product_info['Nome']}\nPreço: {product_info['Preço']}\nPontos: {product_info['Pontos']}"
            )
            print("################################")


### Teste ###1


if __name__ == "__main__":
    bl_teste = Long_band()
    bl_teste.add_product()
    bl_teste.extract_product()


### Teste ###
