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
        self.effect_type = self.__set_effect_type(effect_type)
        self.type = "Spell"

        def __repr__(self):
            return super().__repr__()

    def __set_effect_type(self, effect_type: str):
        if effect_type in [e.value for e in EffectType]:
            return effect_type
        raise ValueError

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state.get("mana")):
            if self.effect_type == EffectType.DAMAGE.value:
                effect = f"Deal {self.cost} damage to target"
            elif self.effect_type == EffectType.HEAL.value:
                effect = f"Heal {self.cost} life to target"
            elif self.effect_type == EffectType.BUFF.value:
                effect = f"Gives {self.cost} health to target"
            elif self.effect_type == EffectType.BUFF.value:
                effect = f"Gives {self.name} to target"
            game_state.update({"mana": game_state["mana"] - self.cost})
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': effect}

    def resolve_effect(self, targets: list) -> dict:
        if len(targets) > 3:
            print("Many targets (max 3)")
            return {}
        elif self.effect_type == EffectType.DAMAGE.value:
            return {'targets': targets,
                    'damage_deal': self.cost,
                    'mana_used': self.cost}
        elif self.effect_type == EffectType.HEAL.value:
            return {'targets': targets,
                    'heath_recovery': self.cost,
                    'mana_used': self.cost}
        elif self.effect_type == EffectType.BUFF.value:
            return {"targets": targets,
                    "health_added": self.cost,
                    "mana_used": self.cost}
        elif self.effect_type == EffectType.DEBUFF.value:
            return {"targets": targets,
                    "health_removed": self.cost,
                    "mana_used": self.cost}

    def get_card_info(self):
        info = super().get_card_info()
        info.update({'type': self.type,
                     'effect_type': self.effect_type})
        return info
