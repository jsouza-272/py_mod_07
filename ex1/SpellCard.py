from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = 'damage'
    HEAL = 'heal'
    BUFF = 'buff'
    DEBUFF = 'debuff'


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self._effect_type = self.__set_effect_type(effect_type)
        self._type = "Spell"

        def __repr__(self):
            return super().__repr__()

    def __set_effect_type(self, effect_type: str):
        if effect_type in [e.value for e in EffectType]:
            return effect_type
        raise ValueError

    def play(self, game_state: dict) -> dict:
        if (self.is_playable(game_state.get("mana")) and
                self in game_state['hand']):
            if self._effect_type == EffectType.DAMAGE.value:
                effect = f"Deal {self._cost} damage to target"
            elif self._effect_type == EffectType.HEAL.value:
                effect = f"Heal {self._cost} life to target"
            elif self._effect_type == EffectType.BUFF.value:
                effect = f"Gives {self._cost} health to target"
            elif self._effect_type == EffectType.DEBUFF.value:
                effect = f"Gives {self._name} to target"
            game_state.update({"mana": game_state["mana"] - self._cost})
            game_state['battlefield'].append(
                game_state['hand'].pop(
                    game_state['hand'].index(self)))
            return {'card_played': self._name,
                    'mana_used': self._cost,
                    'effect': effect}
        return {"error": "Not enough mana!"}

    def resolve_effect(self, targets: list) -> dict:
        if len(targets) > 3:
            print("Many targets (max 3)")
            return {}
        elif self._effect_type == EffectType.DAMAGE.value:
            return {'targets': targets,
                    'damage_deal': self._cost,
                    'mana_used': self._cost}
        elif self._effect_type == EffectType.HEAL.value:
            return {'targets': targets,
                    'heath_recovery': self._cost,
                    'mana_used': self._cost}
        elif self._effect_type == EffectType.BUFF.value:
            return {"targets": targets,
                    "health_added": self._cost,
                    "mana_used": self._cost}
        elif self._effect_type == EffectType.DEBUFF.value:
            return {"targets": targets,
                    "health_removed": self._cost,
                    "mana_used": self._cost}

    def get_card_info(self):
        info = super().get_card_info()
        info.update({'type': self._type,
                     'effect_type': self._effect_type})
        return info
