from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol

class IUnit(ABC):
    @abstractmethod
    def attack(self,target):
        pass
    @abstractmethod
    def move(self,location):
        pass

class MoveBehavior(ABC):
    @abstractmethod
    def move(self,unit: "AbstractUnit",location:str) -> None:
        pass

class AttackBehavior(ABC):
    @abstractmethod
    def attack(self,unit: "AbstractUnit",location:str) -> None:
        pass