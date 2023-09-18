class Pessoa:
    ANO_ATUAL = 2023

    def __init__(self, name, age, id):
        self._name = name
        self._age = age
        self._id = id
        self._cpf = None

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, new_cpf):
        self._cpf = new_cpf

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @age.setter
    def age(self, new_age):
        if new_age < 18:
            raise ValueError("Age must be between")
        self._age = new_age

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    def calculate_year_birth(self):
        return self.ANO_ATUAL - self.age

    def show_data(self):
        return f"Nome:{self.name},Age:{self.age},CPF:{self.cpf}"


p1 = Pessoa("Juan", 21, 271114)
p1.id = 147855
print(p1.id)
print(p1.calculate_year_birth())
p1.age = 90
print(p1.calculate_year_birth())
p1.cpf = 10488775400
print(p1.show_data())
