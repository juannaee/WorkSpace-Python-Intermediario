class Display:
    def display_status(self, final, init):
        bar = "#" * init + " " * (final - init)
        print(f"LOADING... [{bar}] {init}%\r", end="", flush=True)