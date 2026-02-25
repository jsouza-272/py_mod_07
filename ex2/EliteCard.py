from ex0 import Card
from ex0.Card import Rarity
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, combat_type, damage: int,
                 health: int, defense: int,
                 mana: int) -> None:
        super().__init__(name, cost, Rarity.LEGENDARY.value)
        self.combat_type = combat_type
        self.damage = damage
        self.health = health
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get('mana')):
            game_state.update({"mana": game_state["mana"] - self.cost})
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'Elite summoned to battlefield'}

    def attack(self, target: str) -> dict:
        return {'attacker': self.name, 'target': target,
                'damage': self.damage, 'combat_type': self.combat_type}

    def defend(self, imcoming_damage) -> dict:
        damage = abs(self.defense - imcoming_damage)
        alive = True
        if (self.health - damage) <= 0:
            alive = False
        return {'defender': self.name,
                'damage_taken': abs(self.defense - imcoming_damage),
                'damage_blocked': self.defense,
                'still_alive': alive}

    def get_combat_status(self) -> dict:
        return {'health': self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.mana -= self.cost
        return {'caster': self.name,
                'spell': spell_name,
                'targets': targets,
                'mana_used': self.cost}

    def channel_mana(self, amount):
        self.mana += amount
        return {'channeled': amount,
                'total_mana': self.mana}

    def get_magic_stats(self):
        return {'mana_remaining': self.mana}
