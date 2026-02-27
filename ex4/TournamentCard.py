from .Rankable import Rankable
from ex0 import Card
from ex2 import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int,
                 rating: int = 0, wins: int = 0, losses: int = 0) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity,
                         rating=rating, wins=wins, losses=losses)
        self._total_health = health
        self._id = "unregistered"
        self._attack = attack
        self._health = health
        self._defense = defense
        self._win_last = None

    def __repr__(self) -> str:
        return self._id

    def restore(self) -> None:
        self._health = self._total_health

    def play(self, game_state: dict) -> dict:
        if (self.is_playable(game_state['mana'])
                and self in game_state['hand']):

            game_state.update({"mana": game_state["mana"] - self._cost})
            game_state['battlefield'].append(
                game_state['hand'].pop(
                    game_state['hand'].index(self)
                    ))
            return {'card_played': self._name, 'mana_used': self._cost,
                    'effect': 'Creature summoned to battlefield'}
        return {"error": "Not enough mana!"}

    def attack(self, target: 'TournamentCard') -> dict:
        target.defend(self._attack)
        return {'attacker': self._name, 'target': target,
                'damage': self._attack}

    def defend(self, imcoming_damage: int) -> dict:
        damage = (abs(self._defense - imcoming_damage)
                  if self._defense <= imcoming_damage
                  else 0)
        self._health -= damage
        alive = True
        if self._health <= 0:
            alive = False
        return {'defender': self._name,
                'damage_taken': damage,
                'damage_blocked': self._defense,
                'still_alive': alive}

    def get_combat_status(self) -> dict:
        alive = (True if self._health > 0 else False)
        return {'alive': alive}

    def calculate_rating(self) -> int:
        if self._win_last:
            self._rating += 16
        elif not self._win_last and self._rating > 0:
            self._rating -= 16
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._win_last = True
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        self._win_last = False
        self._losses += losses

    def get_rank_info(self) -> dict:
        return {'name': self._name,
                'cost': self._cost,
                'rarity': self._rarity,
                'attack': self._attack,
                'health': self._health,
                'defense': self._defense,
                'rating': self._rating,
                'wins': self._wins,
                'losses': self._losses,
                }
