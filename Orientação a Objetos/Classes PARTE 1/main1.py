class Pessoa:
    def __init__(self, username, password):
        self.username = username
        self.password = password


p1 = Pessoa("Juan", "juan2711")
print(p1.username, p1.password)
