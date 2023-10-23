
"""
📌 Доработаем задачу 1.
📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""
import json
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
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
       with open('fact.json', 'w') as f:
           json.dump(list(self.store), f, indent=2)
              
with Factorial(3) as fact:
    fact(8)
    fact(2)
    fact(4)
    fact(5)
    #print(fact)