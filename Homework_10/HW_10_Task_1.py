# Создание класса-фабрики для животных

# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и 
# добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает 
# категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего 
# (Малявка, Обычный, Гигант) в зависимости от веса.
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе 
# переданного типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal'). 
# *args - переменное количество аргументов, представляющих параметры для конкретного типа животного. 
# Количество и типы аргументов могут различаться в зависимости от типа животного. 
# Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

# Пример

# На входе:

# # Создание экземпляров животных
# animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

# # Вывод результатов
# print(animal1.wing_length())
# print(animal2.depth())
# print(animal3.category())

# На выходе:

# 100.0
# Средневодная рыба
# Гигант

class Animal:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        print(self.name)
        
class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        
        self.max_depth = max_depth
    
    def depth(self):
        if 0 < self.max_depth < 4:
            return 'мелководные'
        elif  4 <= self.max_depth < 8:
            return 'средневодная'
        else:
            return 'глубоководная'
        
    def info(self):
        print('Это Рыбы') 
        
class Bird(Animal):
      
    def __init__(self, name, wingspan):
        super().__init__(name)
        
        self.wingspan = wingspan
        
    def wing_length(self):
        return self.wingspan / 2
    
class Mammal(Animal):
    
    def __init__(self, name, weight):
        super().__init__(name)
        
        self.weight = weight    
    
    def info(self):
        print('Это млекопитающие')
        
    def category(self):
        
        if 1 < self.weight < 10:
            return 'Mалявка'
        elif  10 <= self.weight < 50:
            return 'Обычный'
        else:
            return 'Гигант'
            
class AnimalFactory(Animal):
  
    #@staticmethod
    def create_animal(animal_type: str, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            return 'Тип животного не определен'

# animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
# animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
# animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

# print(animal2.name)
# print(animal1.wing_length())
# print(animal2.depth())
# print(animal3.category())

#print((Bird.__name__)

#   animal_dict = {}
    
#     def create_animal(animal_type: str, *args):
#         if animal_type == 'Bird':
#             return Bird(*args)
#         elif animal_type == 'Fish':
#             return Fish(*args)
#         elif animal_type == 'Mammal':
#             return Mammal(*args)
#         else:
#             return 'Тип животного не определен'


# РЕШЕНИЕ СИСТЕМЫ

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name)
#         self.wingspan = wingspan

#     def wing_length(self):
#         return self.wingspan / 2

# class Fish(Animal):
#     def __init__(self, name, max_depth):
#         super().__init__(name)
#         self.max_depth = max_depth

#     def depth(self):
#         if self.max_depth < 10:
#             return 'Мелководная рыба'
#         elif self.max_depth > 100:
#             return 'Глубоководная рыба'
#         return 'Средневодная рыба'

# class Mammal(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name)
#         self.weight = weight

#     def category(self):
#         if self.weight < 1:
#             return 'Малявка'
#         elif self.weight > 200:
#             return 'Гигант'
#         return 'Обычный'

# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type, *args):
#         if animal_type == 'Bird':
#             return Bird(*args)
#         elif animal_type == 'Fish':
#             return Fish(*args)
#         elif animal_type == 'Mammal':
#             return Mammal(*args)
#         else:
#             raise ValueError('Недопустимый тип животного')


# решение преподавателя

class Animal:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        pass


class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания {self.name} = {self.depth} m'


class Reptiles(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела {self.name} = {self.length} m'


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода кошки {self.name} = {self.breed}'


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода собаки {self.name} = {self.breed}'


class AnimalFactory:
    animal_classes = {
        'Fish': Fish,
        'Reptiles': Reptiles,
        'Cat': Cat,
        'Dog': Dog
    }

    def create_animal(self, animal_type, *args):
        if animal_type not in self.animal_classes:
            raise ValueError("Invalid animal type") # вызов ошибки

        animal_class = self.animal_classes[animal_type]
        return animal_class(*args)




if __name__ == "__main__":
    factory = AnimalFactory()

    fish = factory.create_animal('Fish', 'Goldfish', 0.3)
    reptile = factory.create_animal('Reptiles', 'Snake', 1.5)
    cat = factory.create_animal('Cat', 'Fluffy', 'Persian')
    dog = factory.create_animal('Dog', 'Buddy', 'Labrador')

    print(fish.get_info())
    print(reptile.get_info())
    print(cat.get_info())
    print(dog.get_info())