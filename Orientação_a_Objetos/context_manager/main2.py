from pathlib import Path
from contextlib import contextmanager

FILE_PATH = Path(__file__).parent / "file_2.txt"


class FileManager:
    def __init__(self):
        self._path = None
        self._mode = None
        self._file = None

    @contextmanager
    def open_file(self, path, mode):
        try:
            self._file = open(path, mode, encoding="utf-8")
            yield self._file
        except FileNotFoundError:
            print("Arquivo não existe")
        finally:
            if self._file:
                self._file.close()


teste = FileManager()
with teste.open_file(FILE_PATH, "w") as archiver:
    archiver.write("Teste 2")
