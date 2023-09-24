# АТРИБУТЫ И МЕТОДЫ ОБЪЕКТОВ

# print('Hello world'. __doc__)
# print(str.__doc__)

# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str

# __doc__ - метод. Обращение к методам происходит через точку (.)
# дандер метод (с двойным подчеркиванием) - нужны, чтобы правильно работать с объектами, производить с ними действия
# дандер могут быть и методы, и атрибуты

# print('Hello world'.upper()) # HELLO WORLD
# print('Hello world'.count('l')) # 3 - посчитать сколько раз строка 'l' входит в строку 'Hello world'

# Функции, которые позволяют получить инфо об атрибутах и методах dir(pobject), help(object)

# функция help без аргумента позволяет запустить справочный формат

# print(dir('hello world'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
#  '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
#  'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
#  'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# help('hello world')
# сама эта конкретная строка не имеет собственной документации, ее имеет объект str
# Use help() to get the interactive help utility. 
# Use help(str) for help on the str class.   

# help(str)

# help() # - запускаем интерактивный справочный режим

# help> keywords

# Here is a list of the Python keywords.  Enter any keyword to get more help.

# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not

# help> break    
# help> symbols
# help> %

