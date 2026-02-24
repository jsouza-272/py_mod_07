from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str,
                 cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def __set_rarity(self, rarity) -> str:
        if rarity in [r.value for r in Rarity]:
            return rarity
        raise ValueError

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
