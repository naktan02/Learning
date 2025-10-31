from __future__ import annotations
from ..core.interfaces import AttackBehavior
from ..core.unit import AbstractUnit


class RangedGun(AttackBehavior):
    def attack(self, unit: AbstractUnit, target: str) -> None:
        print(f"[공격] {unit.name} → {target} (원거리 사격, {unit.atk} 피해, 공/지)")


class FlameAttack(AttackBehavior):
    def attack(self, unit: AbstractUnit, target: str) -> None:
        print(f"[공격] {unit.name} → {target} (화염방사, {unit.atk} 피해, 근접-광역)")


class NoAttack(AttackBehavior):
    def attack(self, unit: AbstractUnit, target: str) -> None:
        print(f"[공격] {unit.name}: 공격 불가")