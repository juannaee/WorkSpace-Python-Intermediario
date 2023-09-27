from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / "Log.txt"


class Log(ABC):
    @abstractmethod
    def log(self, message):
        pass

    @abstractmethod
    def log_message(self, message):
        pass


class LogPrint(Log):
    def log(self, message):
        super().log(message)

    def log_message(self, message):
        return f"`{message} Classe = {self.__class__.__name__}"


class LogFile(Log):
    def log(self, message):
        super().log(message)

    def log_message(self, message):
        log_entry = {"message": message, "Classe": self.__class__.__name__}
        for key, value in log_entry.items():
            with open(LOG_FILE, "a") as f:
                f.write(f"{key}: {value}\n".format())


### APENAS PARA TESTES ###


if __name__ == "__main__":
    msg = "Teste_1"
    log_test_print = LogPrint()
    log_test_print.log(msg)
    log_test_print.log_message(msg)
    log_test_save_file = LogFile()
    log_test_save_file.log_message(msg)
    # log_test_1 = Log()
    # print(log_test_1.log_message(msg))


### APENAS PARA TESTES ###
