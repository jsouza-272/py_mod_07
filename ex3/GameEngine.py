from .Cardfactory import CardFactory
from .GameStrategy import GameStrategy
from ex1 import Deck


class GameEngine():
    def __init__(self):
        self._turn_simulated = 0
        self._total_damage = 0
        self._cards_created = 0
        self._factory = None
        self.strategy = None
        self.player = {'hand': [], 'mana': 10, 'battlefield': [],
                       'graveyard': [], 'pile': []}
        self.enemy = {'hand': [], 'mana': 10, 'battlefield': [],
                      'graveyard': [], 'pile': Deck}
        self._game_state = {'player': self.player, 'enemy': self.enemy}

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self.strategy = strategy

        deck1 = Deck()
        deck1.add_card(self._factory.create_spell())
        for i in range(2):
            deck1.add_card(self._factory.create_creature())

        if isinstance(deck1, Deck):
            self._cards_created += deck1.get_deck_status().get('total_cards')
        self.player['pile'] = deck1

        for i in range(0, 3):
            self.player['hand'].append(self.player['pile'].draw_card())
        self.enemy['hand'].append(self._factory.create_creature())

    def simulate_turn(self) -> dict:
        self._turn_simulated += 1
        while len(self.player['hand']) > 1:
            self.player['hand'][0].play(self.player)
        while len(self.enemy['hand']) > 1:
            self.enemy['hand'][0].play(self.enemy)

        self.strategy.prioritize_targets(self.enemy.get('battlefield'))

        battle_result = self.strategy.execute_turn(
            self.player['hand'],
            self.player['battlefield'])

        self._total_damage += battle_result.get('damage_dealt')
        return battle_result

    def get_engine_status(self) -> dict:
        return {'turns_simulated': self._turn_simulated,
                'strategy_used': self.strategy.get_strategy_name(),
                'total_damage': self._total_damage,
                'cards_created': self._cards_created}
