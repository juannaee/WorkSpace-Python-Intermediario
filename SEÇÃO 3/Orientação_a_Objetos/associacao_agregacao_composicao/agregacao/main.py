class ProductCart:
    def __init__(self):
        self.__product = []

    def list_products(self):
        print("================================")
        if not self.__product:
            print("Seu carrinho está vazio...")
        for product in self.__product:
            print(f"Produto: {product.name}\nPreço: {product.price}\n")

        print("================================")

    def add_products(self, *product):
        self.__product.extend(product)
        # for produto in product:
        #     self.__product.append(produto)

    def get_total_price(self):
        return sum([p.price for p in self.__product])


class Product:
    def __init__(self, name, price):
        self.price = price
        self.name = name


class Invoice:
    def generate_invoice(self, product_cart):
        print("================================")
        product_cart.list_products()
        print(f"Preço Total: {product_cart.get_total_price()}")
        print("================================")


p1, p2 = Product("Caneta", 2.50), Product("Tênis", 2.50)
cart_1 = ProductCart()
cart_1.add_products(p1, p2)
invoice_cart_1 = Invoice()
invoice_cart_1.generate_invoice(cart_1)
