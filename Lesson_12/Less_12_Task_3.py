"""
📌 Создайте класс-генератор.
📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
📌 Если переданы два параметра, считаем step=1.
📌 Если передан один параметр, также считаем start=1.
"""
from math import factorial

class Generator:
    
    def __init__(self, start=None, stop=None, step=None):
        if stop is None:
            start, stop = 1, start
        if step is None:
            step = 1
        self.start = start   
        self.stop = stop
        self.step = step
        
    def gener(self):
        for i in range(self.start, self.stop+1, self.step):
            yield factorial(i)
            
g = Generator(2, 8, 2)
for i in g.gener():
    print(i)        