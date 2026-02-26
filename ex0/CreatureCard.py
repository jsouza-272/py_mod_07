from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self._attack = self.__set_attack(attack)
        self._health = self.__set_health(health)
        self._type = "Creature"

    def __repr__(self):
        return super().__repr__()

    def __set_attack(self, attack) -> int:
        if attack < 0:
            raise ValueError
        return attack

    def __set_health(self, health) -> int:
        if health < 0:
            raise ValueError
        return health

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state.get("mana"))
        if playable and self in game_state['hand']:
            game_state.update({"mana": game_state["mana"] - self._cost})
            game_state['battlefield'].append(
                game_state['hand'].pop(
                    game_state['hand'].index(self)))
            return {'card_played': self._name, 'mana_used': self._cost,
                    'effect': 'Creature summoned to battlefield'}
        return {"error": "Not enough mana!"}

    def attack_target(self, target: 'CreatureCard') -> dict:
        combat_resolved = False
        target._health -= self._attack
        if target._health <= 0:
            combat_resolved = True
        return {'attacker': self._name,
                'target': target._name,
                'damage_dealt': self._attack,
                'combat_resolved': combat_resolved}

    def get_card_info(self):
        info = super().get_card_info()
        info.update({"type": self._type,
                     "attack": self._attack,
                     "health": self._health})
        return info
