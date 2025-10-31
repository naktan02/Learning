from __future__ import annotations
from typing import Callable, Dict, List, TypeVar
from .unit import AbstractUnit

class Race:
    def __init__(self,name: str) -> None:
        self.name = name,
        self.units: List[AbstractUnit] = []
        self._registry = {}
    
    def register(self,key:str,builder):
        k = key.lower()
        if k in self._registry:
            raise KeyError(f"이미 등록된 유닛: {key}")
        self._registry[k] = builder
    
    def train(self,key:str,*args, **kwargs):
        k = key.lower()
        if k not in self._registry:
            raise ValueError(f"{self.name}: 미등록 유닛 '{key}'")
        unit = self._registry[k](*args, **kwargs)   # ← 인자를 그대로 전달
        self.units.append(unit)
        print(f"[생산] {self.name}: {unit.name} 생성")
        return unit