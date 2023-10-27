from pathlib import Path

FILE_PATH = Path(__file__).parent / "file.txt"


class OpenFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print("Abrindo arquivo")
        self._file = open(self.path, self.mode, encoding="utf-8")
        return self._file

    def __exit__(self, class_execption, execption_, traceback_):
        self._file.close()


with OpenFile(FILE_PATH, "w") as archive:
    archive.write("Teste 1")
