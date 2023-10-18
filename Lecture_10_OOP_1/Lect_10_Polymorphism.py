# ПОЛИМОРФИЗМ

"""Например сложение чисел
возвращает их сумму, а сложение строк возвращает новую строку состоящую из
двух исходных. Одинаковые действия приводят к разному, но ожидаемому
результату."""

class Person:
    
    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3
        
    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity
    ...
    
class Hero(Person):
    def __init__(self, power, *args, **kwargs):
        self.power = power
        super().__init__(*args, **kwargs)
        
    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2
    ...
    
p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
p2 = Person('Маг', 'Тролль')
print(f'{p1.health = }, {p2.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }')
p2.change_health(p1, 10)
print(f'{p1.health = }, {p2.health = }')

# p1.health = 100, p2.health = 100
# p1.health = 120, p2.health = 80
# p1.health = 110, p2.health = 90

"""Один и тот же метод change_health по разному меняет параметр health у обычного
персонажа и у героя."""

# ДЕЛЕНИЕ СТРОК - еще 1 вариант полиморфизма

# path_1 = '/home/user'
# path_2 = '/my_project/workdir'
# result = path_1 / path_2 # TypeError: unsupported operand type(s) for /: 'str' and 'str'

"""Python не поддерживает деление строк. Но мы уже сталкивались с тем как класс
Path из модуля pathlib создавал новый путь используя символ деления. Реализовать
подобный полиморфизм можно например так."""

class DivStr(str):
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj
        
        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, DivStr):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)
            
        if first and second:
            return DivStr(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return DivStr(start + finish)
        if not first and not second:
            return DivStr(start + '/' + finish)
        
path_1 = DivStr('/home/user/')
path_2 = DivStr('/my_project/workdir')
result = path_1 / path_2
print(f'{result = }, {type(result)}')
# result = '/home/user/my_project/workdir', <class '__main__.DivStr'>

print(f'{result / "text" = }')
# result / "text" = '/home/user/my_project/workdir/text'

print(f'{result / 42 = }')
# result / 42 = '/home/user/my_project/workdir/42'

print(f'{result * 3 = }')
# result * 3 = '/home/user/my_project/workdir/home/user/my_project/workdir/
# home/user/my_project/workdir'

"""Создаём класс DivStr как наследник класса str. При инициализации определяем
аргумент obj, который является обычной строкой. Вся магия деления строк будет
спрятана в магическом методе __truediv__ который срабатывает при делении
экземпляра класса DivStr на другой такой же экземпляр или на обычную строку str:
"""

