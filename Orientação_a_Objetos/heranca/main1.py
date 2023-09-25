class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def point_class(self):
        print(f"Classe atual: {self.__class__.__name__}")

    def hello(self):
        print(f"Hello {self.__class__.__name__}")


class Employee(Person):
    def __init__(self, name, surname, id):
        super().__init__(name, surname)
        self.id = id

    def hello(self):
        super().hello()


person_1 = Employee("Teste 1", "Teste 1 ", 271114)
person_1.point_class()
person_1.hello()
person_2 = Person("Teste 2", "Teste 2 ")
person_2.hello()
