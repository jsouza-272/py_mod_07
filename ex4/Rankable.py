from abc import ABC, abstractmethod


class Rankable(ABC):
    def __init__(self, rating: int = 0, wins: int = 0,
                 losses: int = 0, **kwargs: dict) -> None:
        super().__init__(**kwargs)
        self._wins = wins
        self._losses = losses
        self._rating = rating

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
