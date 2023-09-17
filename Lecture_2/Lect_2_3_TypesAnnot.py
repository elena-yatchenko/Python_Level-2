# АННОТАЦИЯ ТИПОВ (тайпхинтинг) - не является обязательной. НО - правило хорошего тона

# a: int = 42
# b: float = float(input('enter number: '))
# a = a / b
# print(a)

# Более полезна аннотация типов при создании функций. Помогает лучше понимать код (что хотим получить и вернуть)

# def my_func(data: list[int, float]) -> float:
#     res = sum(data) / len(data)
#     return(res)

# print(my_func([2, 5.5, 15, 8.8, 13.74]))

# в пайтон начиная с версии 3.10 можно задавать несколько типов с помощью вертикальной черты |, которая значит "или"
a: int | float = 42

# в питоне есть модуль typing (import typing), из которого можно брать инфо о типах данных

