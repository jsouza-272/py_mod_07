from .GameStrategy import GameStrategy
from ex0 import CreatureCard
from ex1 import SpellCard


class AggressiveStrategy(GameStrategy):
    def __init__(self):
        self._strategy_name = "AggressiveStrategy"
        self._targets = []

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_used = sum([card._cost for card in battlefield])

        spell_damage = 0
        for card in battlefield:
            if isinstance(card, SpellCard):
                card.resolve_effect(self._targets)
                spell_damage += card._cost * len(self._targets)

        creature_damage = 0
        for card in battlefield:
            if isinstance(card, CreatureCard):
                card.attack_target(self._targets[0])
                creature_damage += card._attack

        return {'cards_played': battlefield,
                'mana_used': mana_used,
                'targets_attacked': self._targets,
                'damage_dealt': spell_damage + creature_damage}

    def get_strategy_name(self) -> str:
        return self._strategy_name

    def prioritize_targets(self, available_targets: list) -> list:
        if len(available_targets) < 0:
            print("No target to add")
            return []
        self._targets.extend(available_targets)
        return self._targets
