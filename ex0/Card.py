from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int,
                 rarity: str, **kwargs: dict) -> None:
        super().__init__(**kwargs)
        self._name = name
        self._cost = cost
        self._rarity = self.__set_rarity(rarity)

    def __repr__(self):
        return f"{self._name} ({self._cost})"

    def __set_rarity(self, rarity) -> str:
        try:
            if rarity in [r.value for r in Rarity]:
                return rarity
            raise ValueError("Invalid Rarity")
        except ValueError as error:
            print(error)
            print("Set Rarity to Common")
            self._rarity = Rarity.COMMON.value

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self._name,
                "cost": self._cost,
                "rarity": self._rarity}

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self._cost
