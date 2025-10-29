from abc import ABC, abstractclassmethod

class Race(ABC):
    def __init__(self,name):
        self.name = name
        self.unit = []
    
    @abstractclassmethod
    def train_unit(self):
        pass
    
    @abstractclassmethod
    def special_ability(self):
        pass
