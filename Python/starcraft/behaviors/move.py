from __future__ import annotations
from ..core.interfaces import MoveBehavior
from ..core.unit import AbstractUnit


class GroundMove(MoveBehavior):
    def move(self,unit:AbstractUnit, location:str) -> None:
        print(f"[이동] {unit.name} → {location} (지상, 속도 {unit.speed})")

class FastGroundMove(MoveBehavior):
    def move(self, unit: AbstractUnit, location: str) -> None:
        print(f"[이동] {unit.name} → {location} (지상-가속, 속도 {unit.speed})")


class AirMove(MoveBehavior):
    def move(self,unit: AbstractUnit, location:str) -> None:
        print(f"[이동] {unit.name} → {location} (공중, 속도 {unit.speed})")