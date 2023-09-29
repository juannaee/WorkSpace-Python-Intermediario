from log import LogFile
from abc import ABC, abstractmethod

import time


SLEEP_TIME = 0.03
BATTERY_FULL = 100


class Electronics(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._connected = False
        self._log = LogFile()
        self.battery = 0

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def charge_battery(self):
        pass


class Smartphone(Electronics):
    def connect(self):
        if self.battery == 0:
            self._log.log_message("You must charge the device before turning it on.")
            raise ValueError("You must charge the device before turning it on.")
        if not self._connected:
            self._connected = True

            self._log.log_message("Connecting to Smartphone")

    def disconnect(self):
        if self._connected:
            self._connected = False
            self._log.log_message("disconnect smartphone")

    def charge_battery(self):
        for i in range(BATTERY_FULL + 1):
            time.sleep(SLEEP_TIME)
            self.battery = i
            self.display_battery_status(i)

        print("\nLoaded success 100%")
        return self.battery

    def display_battery_status(self, percentage):
        bar = "#" * percentage + " " * (BATTERY_FULL - percentage)
        print(f"LOADING... [{bar}] {percentage}%\r", end="", flush=True)


if __name__ == "__main__":
    teste_1 = Smartphone("teste_1")
    progresso = teste_1.charge_battery()
    teste_1._connected
