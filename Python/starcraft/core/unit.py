from __future__ import annotations
from typing import List
from .interfaces import IUnit, MoveBehavior, AttackBehavior

class AbstractUnit(IUnit):
    def __init__(
            self,
            name: int,
            hp: int,
            speed: int,
            atk: int,
            move_behavior: MoveBehavior,
            attack_behavior: AttackBehavior
        ) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
        self.speed = speed
        self.atk = atk
        self.move_behavior = move_behavior
        self.attack_behavior = attack_behavior
        
    def set_move_behavior(self, new_move_behavior: MoveBehavior) -> None:
        print(f"[전략변경] {self.name} 이동전략 → {new_move_behavior.__class__.__name__}")
        self.move_behavior = new_move_behavior

    def set_attack_behavior(self, new_attack_behavior: AttackBehavior) -> None:
        print(f"[전략변경] {self.name} 공격전략 → {new_attack_behavior.__class__.__name__}")
        self.attack_behavior = new_attack_behavior

    def move(self, location: str):
        self.move_behavior.move(self,location)
    
    def attack(self, target: str):
        self.attack_behavior.attack(self,target)

    def damaged(self,damage: int) -> None:
        self.hp -=damage
        if self.hp <= 0:
            self.hp = 0
            print(f"[피해] {self.name} {damage} 피해 → 사망")
        else:
            print(f"[피해] {self.name} {damage} 피해 → HP {self.hp}")

