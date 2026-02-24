from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = self.__set_attack(attack)
        self.health = self.__set_health(health)
        self.type = "Creature"

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
        if playable:
            print(f"Playable: {playable}")
            game_state.update({"mana": game_state["mana"] - self.cost})
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        print(f"Playable: {playable}")
        return None

    def attack_target(self, target: 'CreatureCard') -> dict:
        combat_resolved = False
        target.health -= self.attack
        if target.health <= 0:
            combat_resolved = True
        return {'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolved': combat_resolved}

    def get_card_info(self):
        info = super().get_card_info()
        info.update({"type": self.type,
                     "attack": self.attack,
                     "health": self.health})
        return info
