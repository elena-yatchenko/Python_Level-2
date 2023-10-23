# МОДУЛЬ DEQUE

Основное использование deque
Основные методы, которые полезны с этим классом являются popleft и appendleft

from collections import deque

d = deque([1, 2, 3])
p = d.popleft()        # p = 1, d = deque([2, 3])
d.appendleft(5)        # d = deque([5, 2, 3]) 
Ограничение размера deque
Используйте maxlen параметр при создании Deque ограничить размер дека:

from collections import deque
d = deque(maxlen=3)  # only holds 3 items
d.append(1)  # deque([1])
d.append(2)  # deque([1, 2])
d.append(3)  # deque([1, 2, 3])
d.append(4)  # deque([2, 3, 4]) (1 is removed because its maxlen is 3) 
Доступные методы в deque
Создание пустой декы:

dl = deque()  # deque([]) creating empty deque
Создание дек с некоторыми элементами:

dl = deque([1, 2, 3, 4])  # deque([1, 2, 3, 4])
Добавление элемента в deque:

dl.append(5)  # deque([1, 2, 3, 4, 5]) 
Добавление элемента левой стороны deque:

dl.appendleft(0)  # deque([0, 1, 2, 3, 4, 5])
Добавление списка элементов в deque:

dl.extend([6, 7])  # deque([0, 1, 2, 3, 4, 5, 6, 7])
Добавление списка элементов с левой стороны:

dl.extendleft([-2, -1])  # deque([-1, -2, 0, 1, 2, 3, 4, 5, 6, 7])
Использование .pop() элемента естественно удалить элемент с правой стороны:

dl.pop()  # 7 => deque([-1, -2, 0, 1, 2, 3, 4, 5, 6])
Используя .popleft() элемент , чтобы удалить элемент с левой стороны:

dl.popleft()  # -1 deque([-2, 0, 1, 2, 3, 4, 5, 6])
Удалить элемент по его значению:

dl.remove(1)  # deque([-2, 0, 2, 3, 4, 5, 6]) 
Обратный порядок элементов в deque:

dl.reverse()  # deque([6, 5, 4, 3, 2, 0, -2])
Ширина Первый Поиск
Deque является единственной структурой данных Python с быстрой Очереди операций.(Примечание queue.Queue обычно не подходит, так как он предназначен для связи между потоками.) Основной случай использования из очереди является поиск в ширину .

from collections import deque

def bfs(graph, root):
    distances = {}
    distances[root] = 0
    q = deque([root])
    while q:
        # Самый старый замеченный (но еще не посещенный) узел будет самым левым.
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                # Когда мы видим новый узел, мы добавляем его в правую часть очереди.
                q.append(neighbor)
    return distances
Скажем, у нас есть простой ориентированный граф:

graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]} 
Теперь мы можем найти расстояния от некоторой начальной позиции:

>>> bfs(graph, 1)
{1: 0, 2: 1, 3: 1, 4: 2, 5: 2}

>>> bfs(graph, 3)
{3: 0, 4: 1, 5: 1}