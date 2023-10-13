import abc
from display import Display


def display_img(msg_img):
    print(Display.display_status(final=100, init=1, msg=msg_img))


class Account(abc.ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance
        self.total_balance = None

    @abc.abstractmethod
    def withdraw(self, value_withdraw):
        ...

    def deposit(self, value_deposit):
        display_img("Depositando.....")
        self.total_balance = self.balance + value_deposit
        return self.total_balance

    def details(self):
        return f"Detalhes da Conta:\nSaldo Atual: R$ {self.total_balance:.2f}"


class Teste(Account):
    def __init__(self, agency, account, balance):
        super().__init__(agency, account, balance)

    def withdraw(self, value_withdraw):
        return super().withdraw(value_withdraw)

    def deposit(self, value_deposit):
        return super().deposit(value_deposit)

    def details(self):
        return super().details()


if __name__ == "__main__":
    teste = Teste("teste", "teste", 100)
    teste.deposit(2500)
    print(teste.details())
