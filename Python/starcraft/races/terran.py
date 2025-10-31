from __future__ import annotations
from typing import List
from ..core.unit import AbstractUnit
from ..core.race import Race
from ..behaviors.move import GroundMove, FastGroundMove, AirMove
from ..behaviors.attack import RangedGun, NoAttack


class Marine(AbstractUnit):
    def __init__(self, name="Marine", hp=100, speed=5, atk=5):
        super().__init__(
            name=name,
            hp=hp,
            speed=speed,
            atk=atk,
            move_behavior=GroundMove(),
            attack_behavior=RangedGun()
        )
    
    def use_stimpack(self) -> None:
        print("[스킬] Marine: Stimpack 사용! (HP -10, 속도/공격력 증가 가정)")
        self.damaged(10)
        self.speed += 2
        self.atk += 2
        self.set_move_behavior(FastGroundMove())

class Dropship(AbstractUnit):
    def __init__(self, name="Dropship", hp=200, speed=7, atk=0):
        super().__init__(
            name=name,
            hp=hp,
            speed=speed,
            atk=atk,
            move_behavior=AirMove(),
            attack_behavior=NoAttack(),
        )
        self.capacity = 8
        self.cargo: List[AbstractUnit] = []
    
    def load(self, unit: AbstractUnit) -> None:
        if len(self.cargo) >= self.capacity:
            print(f"[수송] {self.name}: 적재 한도 초과")
            return
        self.cargo.append(unit)
        print(f"[수송] {self.name}: {unit.name} 탑승 ({len(self.cargo)}/{self.capacity})")

    def unload_all(self) -> None:
        if not self.cargo:
            print(f"[수송] {self.name}: 탑승 유닛 없음")
            return
        names = ", ".join(u.name for u in self.cargo)
        print(f"[수송] {self.name}: 하차 → {names}")
        self.cargo.clear()


class Terran(Race):
    def __init__(self):
        super().__init__("Terran")
        self.register("marine", Marine)
        self.register("dropship", Dropship)
