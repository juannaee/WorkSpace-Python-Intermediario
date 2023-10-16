SLEEP_TIME = 0.01
import time


class Display:
    def display_status(final, init, msg):
        for init in range(final + 1):
            time.sleep(SLEEP_TIME)
            bar = "#" * init + " " * (final - init)
            print(f"{msg}... [{bar}] {init}%\r", end="", flush=True)


if __name__ == "__main__":
    Display.display_status(100, 1, "testando...........")
