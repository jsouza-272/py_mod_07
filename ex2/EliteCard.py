from ex0 import Card
from ex0.Card import Rarity
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, combat_type, damage: int,
                 health: int, defense: int,
                 mana: int) -> None:
        super().__init__(name, cost, Rarity.LEGENDARY.value)
        self._combat_type = combat_type
        self._damage = damage
        self._health = health
        self._defense = defense
        self._mana = mana

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get('mana')):
            game_state.update({"mana": game_state["mana"] - self._cost})
            return {'card_played': self._name, 'mana_used': self._cost,
                    'effect': 'Elite summoned to battlefield'}

    def attack(self, target: str) -> dict:
        return {'attacker': self._name, 'target': target,
                'damage': self._damage, 'combat_type': self._combat_type}

    def defend(self, imcoming_damage) -> dict:
        damage = abs(self._defense - imcoming_damage)
        alive = True
        if (self._health - damage) <= 0:
            alive = False
        return {'defender': self._name,
                'damage_taken': abs(self._defense - imcoming_damage),
                'damage_blocked': self._defense,
                'still_alive': alive}

    def get_combat_status(self) -> dict:
        return {'health': self._health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self._mana -= self._cost
        return {'caster': self._name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': self._cost}

    def channel_mana(self, amount):
        self._mana += amount
        return {'channeled': amount,
                'total_mana': self._mana}

    def get_magic_stats(self):
        return {'mana_remaining': self._mana}
