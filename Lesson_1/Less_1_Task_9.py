# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 10):
    for j in range(2, 11):
        print(str(i) + '*' + str(j))

# в виде таких блоков как в школьной тетради не смогла придумать как :((((
    
    
    # for i in range(2, 11):
    # for j in range(2, 6):
    #     print(f"{j} x {i} = {j * i}\t", end="")
    # print("\t", end="")
    # for j in range(6, 10):
    #     print(f"{j} x {i} = {j * i}\t", end="")
    # print()