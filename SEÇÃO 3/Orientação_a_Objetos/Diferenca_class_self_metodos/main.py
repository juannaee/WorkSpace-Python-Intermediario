class Connection:
    def __init__(self, host="Localhost"):
        self.host = host
        self.username = None
        self.password = None

    def set_user(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    @classmethod
    def created_whith_auth(cls, username, password):
        connection = cls()
        connection.username = username
        connection.password = password
        return connection


c1 = Connection()
c1.set_user("Juan_aeee")
c1.set_password("Juan@2711")
print(f"{c1.username}\n{c1.password}")


c2 = Connection.created_whith_auth("Bianca_aeee", "Bian@2711")
print(f"{c2.username}\n{c2.password}")
