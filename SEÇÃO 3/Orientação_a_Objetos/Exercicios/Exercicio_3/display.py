SLEEP_TIME = 0.01
import time


class Display:
    @staticmethod
    def display_status(final: int, init: int, msg: str) -> str:
        for progress in range(init, final + 1):
            time.sleep(SLEEP_TIME)
            bar = "#" * progress + " " * (final - progress)
            print(f"{msg}... [{bar}] {progress}%\r", end="", flush=True)


if __name__ == "__main__":
    Display.display_status(100, 1, "testando.................")
