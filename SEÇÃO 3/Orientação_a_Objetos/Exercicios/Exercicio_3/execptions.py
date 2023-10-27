import sys


class ExceptHandle:
    def __init__(self) -> None:
        pass

    def execept_value_error(self, value):
        try:
            int(value)
        except ValueError:
            print(f"ERROR EM: {self.__name__}\nMotivo: inserir valores numéricos")
            sys.exit()

        except:
            print(f"ERROR:{__name__}")
            sys.exit()
