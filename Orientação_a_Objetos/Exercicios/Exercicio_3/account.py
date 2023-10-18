import abc
from display import Display
from execptions import ExceptHandle


def display_img(msg_img: str):
    print(Display.display_status(final=100, init=1, msg=msg_img))


class Account(abc.ABC):
    def __init__(self, agency: int, account: int, balance: float) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance
        self.total_balance = balance
        self.value_deposit = 0
        self.value_withdraw = 0
        self.historical_transition = []

    @abc.abstractmethod
    def withdraw(self, value_withdraw: float):
        ...

    def deposit(self, value_deposit: float):
        ExceptHandle.execept_value_error(self.deposit, value_deposit)
        self.value_deposit = value_deposit
        display_img("Depositando.....")
        if value_deposit:
            self.total_balance = self.balance + value_deposit
            transition = f"Deposito de R$ {value_deposit:.2f}"
            self.historical_transition.append(transition)

    def details(self) -> str:
        deposit_details = (
            f" {'R$ ' + str(round(self.value_deposit,2))}"
            if self.value_deposit
            else " Não houve depositos"
        )
        if self.value_withdraw > 0:
            withdraw_details = f" {'R$ ' + str(round(self.value_withdraw,2))}"
        else:
            withdraw_details = " Não houve saque"
        if self.value_withdraw < self.total_balance:
            withdraw_details = "Saque indisponivel,Saldo insuficiente!"

        current_balance = f"R$ {round(self.total_balance,2)}"

        transition_details = "\n".join(self.historical_transition)

        return (
            f"Historico da conta:"
            f"\nSaldo pré deposito / saque: R$ {self.balance}"
            f"\nValor depositado:{deposit_details}"
            f"\nValor sacado:{withdraw_details}"
            f"\nSaldo atual:{current_balance}\n"
            f"\nHistorico de transições: {transition_details}"
        )


class Teste(Account):
    def __init__(self, agency, account, balance):
        super().__init__(agency, account, balance)

    def deposit(self, value_deposit):
        return super().deposit(value_deposit)

    def withdraw(self, value_withdraw):
        ExceptHandle.execept_value_error(self.withdraw, value_withdraw)
        if self.total_balance >= value_withdraw:
            self.total_balance -= value_withdraw
            self.value_withdraw = value_withdraw
            transition = f"Saque de: R$ {value_withdraw:.2f}"
            self.historical_transition.append(transition)

    def details(self):
        return super().details()


if __name__ == "__main__":
    teste = Teste("teste", "teste", 1000)
    teste.deposit(500)
    teste.withdraw("teste")
    print(teste.details())
