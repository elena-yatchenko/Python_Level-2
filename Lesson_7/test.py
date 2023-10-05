from random import randint

print(bytes(randint(0, 255) for i in range(min_size, max_size)))