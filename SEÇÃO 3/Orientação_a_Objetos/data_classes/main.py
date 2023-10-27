from dataclasses import dataclass


@dataclass
class Person:
    name: str
    urname: str
    age: int
    id: int

    def details(self) -> str:
        return f"{self.name},{self.age},{self.id}"

    @property
    def name_completed(self):
        return self.name, self.urname

    @name_completed.setter
    def name_completed(self, value):
        name, *urname = value.split()
        self.name = name
        self.urname = " ".join(urname)


p1 = Person("JUAN", "GUILHERME", 21, 2711)
print(p1)
p1.name_completed = "Juan Guilherme Silva Lemos"
print(*p1.name_completed)
