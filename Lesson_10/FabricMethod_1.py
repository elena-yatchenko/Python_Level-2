# https://refactoring.guru/ru/design-patterns/factory-method

"""Пример работы фабричного метода """

class IProduct:
    def release(self):
        pass
    
class Car(IProduct):
    def release(self):
        print('Выпущен новый легковой автомобиль')
        
class Track(IProduct):
    def release(self):
        print('Выпущен новый грузовой автомобиль')
        
class IWorkShop:
    def create(self) -> IProduct:
        pass

class CarWorkShop(IWorkShop):
    def create(self): # метод создает экземпляр класса Car
        return Car()
    
class TrackWorkShop(IWorkShop):
    def create(self):
        return Track()
    
if __name__ == '__main__':
    creator = CarWorkShop()
    car = creator.create()
    
    creator = TrackWorkShop()
    track = creator.create()
    
    car.release()
    track.release() 
