from typing import Any


class Multiplication:
    def __init__(self, multiplier) -> None:
        self.multiplier = multiplier

    def __call__(self, func):
        def intern(*args, **kwargs):
            result = func(*args, **kwargs)
            result *= self.multiplier
            return result

        return intern


@Multiplication(10)
def sum_test(x, y):
    return x + y


result_1 = sum_test(2, 2)
print(result_1)
