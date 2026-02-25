from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artefact"

    def play(self, game_state: str) -> dict:
        if self.is_playable(game_state.get('mana')):
            game_state.update({"mana": game_state["mana"] - self.cost})
            return {'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect}

    def activate_ability(self) -> dict:
        return {'atefact_used': self.name,
                'effect_applied': self.effect}
