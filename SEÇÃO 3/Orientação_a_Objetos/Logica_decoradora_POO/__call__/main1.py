from typing import Any


class CallMe:
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number

    def __call__(self, dd, *args: Any, **kwds: Any) -> Any:
        print(f"Discando: ({dd}) {self.phone_number}")


test_number = CallMe(996272911)
test_number(81)
