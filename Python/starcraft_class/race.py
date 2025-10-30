from abc import ABC, abstractmethod


class IUnit(ABC):
    @abstractmethod
    def attack(self,target):
        pass
    @abstractmethod
    def move(self,location):
        pass

class AbstractUnit(IUnit):
    def __init__(self,hp,name,speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print(f"{self.name}이(가) {location}으로 이동합니다. (속도 {self.speed})")


    
