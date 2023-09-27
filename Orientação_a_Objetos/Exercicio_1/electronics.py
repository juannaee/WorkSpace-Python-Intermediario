from log import LogFile
from abc import ABC, abstractmethod


class Electronics(ABC):
    def __init__(self, nome):
        self._nome = nome
        self._connected = False
        self._log = LogFile()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class Smartphone(Electronics):
    def connect(self):
        if not self._connected:
            self._connected = True
            self._log.log_message("Connecting to Smartphone")

    def disconnect(self):
        if self._connected:
            self._connected = False
            self._log.log_message("disconnect smartphone")
