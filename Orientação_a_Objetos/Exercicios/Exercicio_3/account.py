import abc
from display import Display


def display_img(msg_img):
    print(Display.display_status(final=100, init=1, msg=msg_img))


class Account(abc.ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance
        self.total_balance = balance
        self.value_deposit = 0
        self.value_withdraw = 0

    @abc.abstractmethod
    def withdraw(self, value_withdraw):
        ...

    def deposit(self, value_deposit):
        self.value_deposit = value_deposit
        display_img("Depositando.....")
        if value_deposit:
            self.total_balance = self.balance + value_deposit

    def details(self):
        deposit_details = (
            f" {'R$ ' + str(round(self.value_deposit,2))}"
            if self.value_deposit
            else " Não houve depositos"
        )
        withdraw_details = (
            f" {'R$ ' + str(round(self.value_withdraw,2))}"
            if self.value_withdraw
            else " Não houve saque"
            if self.value_withdraw < self.total_balance
            else " Saque indisponivel,Saldo insuficiente!"
        )

        current_balance = f"R$ {round(self.total_balance,2)}"

        return (
            f"Historico da conta:"
            f"\nSaldo pré deposito / saque: R$ {self.balance}"
            f"\nValor depositado:{deposit_details}"
            f"\nValor sacado:{withdraw_details}"
            f"\nSaldo atual:{current_balance}"
        )


class Teste(Account):
    def __init__(self, agency, account, balance):
        super().__init__(agency, account, balance)

    def deposit(self, value_deposit):
        return super().deposit(value_deposit)

    def withdraw(self, value_withdraw):
        if self.total_balance >= value_withdraw:
            self.total_balance -= value_withdraw
        self.value_withdraw = value_withdraw

    def details(self):
        return super().details()


if __name__ == "__main__":
    teste = Teste("teste", "teste", 1000)
    teste.deposit(500)
    teste.withdraw(1000)
    print(teste.details())
