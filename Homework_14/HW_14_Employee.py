class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(
        self,
        last_name: str,
        first_name: str,
        patronymic: str,
        age: int,
        position: str,
        salary: float,
    ):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary = round(self.salary * (1 + percent / 100), 1)

    def __str__(self):
        return f"{self.full_name()} ({self.position})"
