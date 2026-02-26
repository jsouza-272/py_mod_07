from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self._durability = durability
        self._effect = effect
        self._type = "Artefact"

        def __repr__(self):
            return super().__repr__()

    def play(self, game_state: dict) -> dict:
        if (self.is_playable(game_state.get('mana'))
                and self in game_state['hand']):
            game_state.update({"mana": game_state["mana"] - self._cost})
            game_state['battlefield'].append(
                game_state['hand'].pop(
                    game_state['hand'].index(self)))
            return {'card_played': self._name,
                    'mana_used': self._cost,
                    'effect': self._effect}
        return {"error": "Not enough mana!"}

    def activate_ability(self) -> dict:
        return {'atefact_used': self._name,
                'effect_applied': self._effect}
