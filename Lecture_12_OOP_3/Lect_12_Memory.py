# ЭКОНОМИМ ПАМЯТЬ

"""Мы уже несколько раз сталкивались с дандер словарём __dict__. Его
предназначение — хранить атрибуты и их значения у каждого объекта Python."""

# ХРАНИТЕЛЬ АТРИБУТОВ __DICT__ (на примере треугольника)

from math import sqrt 

# class Triangle:
    
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
        
#     def __str__(self):
#         return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
            
#     def __repr__(self):
#         return f'Triangle({self._a}, {self._b}, {self._c})'
    
#     def __eq__(self, other):
#         first = sorted((self._a, self._b, self._c))
#         second = sorted((other._a, other._b, other._c))
#         return first == second
    
#     def area(self):
#         p = (self._a + self._b + self._c) / 2
#         _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
#         return _area
    
#     def __lt__(self, other):
#         return self.area() < other.area()
    
#     def __hash__(self):
#         return hash((self._a, self._b, self._c))
    
# triangle = Triangle(3, 4, 5)
# print(triangle)
# # Треугольник со сторонами: 3, 4, 5

# print(triangle.__dict__)
# # {'_a': 3, '_b': 4, '_c': 5}

# print(Triangle.__dict__)
# # {'__module__': '__main__', '__init__': <function Triangle.__init__ at 0x000001A389565760>, '__str__': <function Triangle.__str__ at 0x000001A3895658A0>, '__repr__': <function Triangle.__repr__ at 0x000001A3895656C0>, '__eq__': <function Triangle.__eq__ at 0x000001A3895659E0>, 'area': <function Triangle.area at 0x000001A389565C60>, '__lt__': <function Triangle.__lt__ at 0x000001A389565EE0>, '__hash__': <function Triangle.__hash__ at 0x000001A389566CA0>, '__dict__': <attribute '__dict__' of 'Triangle' objects>, '__weakref__': <attribute '__weakref__' of 'Triangle' objects>, '__doc__': None}

"""Как видите экземпляр хранить лишь три свойства, определённые внутри метода
инициализации. За всем остальным он обращается к своему классу.

Что касается класса, его словарь хранит имена и адреса дандеров, методов и даже пустой
дандер __doc__, ведь мы не сделали строку документации.
При редкой необходимости можно обращаться к ключам словаря для получения
или изменения значений"""

# ЭКОНОМИЯ ПАМЯТИ, __SLOTS__

"""При создании класса можно явно указать перечень имён свойств (КОРТЕЖ СВОЙСТВ), 
которые в нём будут использоваться."""

class Triangle:
    __slots__ = ('_a', '_b', '_c')
    
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
            
    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'
    
    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second
    
    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __hash__(self):
        return hash((self._a, self._b, self._c))
    
triangle = Triangle(3, 4, 5)
# print(triangle.__dict__) # AttributeError: 'Triangle' object has no attribute '__dict__'. Did you mean: '__dir__'?
print(Triangle.__slots__)

# ('_a', '_b', '_c')

"""Коротко о том, что даёт замена изменяемого __dict__ на неизменяемый __slots__?
1. Обеспечивает немедленное обнаружение ошибок из-за неправильного
написания атрибутов. Допускаются только имена атрибутов, указанные в
__slots__
2. Помогает создавать неизменяемые объекты, в которых дескрипторы
управляют доступом к закрытым атрибутам, хранящимся в __slots__
3. Экономит память. В 64-битной сборке Linux экземпляр с двумя атрибутами
занимает 48 байт со __slots__ и 152 байт без него. Экономия памяти имеет
значение только тогда, когда будет создано большое количество
экземпляров.
4. Улучшает скорость. По данным на Python 3.10 на процессоре Apple M1 чтение
переменных экземпляра выполняется на 35% быстрее со __slots__().
5. Блокирует такие инструменты как functools.cached_property(), которым для
правильной работы требуется экземплярный словарь."""