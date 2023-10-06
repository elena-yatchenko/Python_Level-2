from random import randint

print(type(bytes(randint(0, 255) for i in range(256, 4096))))
print(bytes(randint(0, 255) for i in range(256, 4096)))