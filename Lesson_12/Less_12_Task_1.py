# https://www.codecamp.ru/blog/python-deque-module/

"""
📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌 Экземпляр должен запоминать последние k значений.
📌 Параметр k передаётся при создании экземпляра.
📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов."""

from collections import deque

class Factorial:
    
    def __init__(self, k):
        self.store = deque(maxlen=k)
        
    def __call__(self, number):
        result = 1
        for i in range(2, number+1):
            result *= i
        self.store.append({number: result})
        return result

    def __str__(self):
        return f'{self.store}'
    
fact = Factorial(2)
print(fact(5))
print(fact(3))
print(fact(4))
print(fact)
        
        
