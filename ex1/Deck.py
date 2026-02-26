from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
import random


class Deck():
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._cards:
            if card._name == card_name:
                self._cards.remove(card_name)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        if len(self._cards) > 0:
            return self._cards.pop(0)

    def get_deck_status(self) -> dict:
        status = {'total_card': 0,
                  'creatures': 0,
                  'spells': 0,
                  'artifacts': 0,
                  'avg_cost': 0}
        try:
            total_cost = sum([card._cost
                              for card in self._cards])
            total_cards = len(self._cards)
            total_creatures = len([card for card in self._cards
                                   if isinstance(card, CreatureCard)])
            total_spells = len([card for card in self._cards
                                if isinstance(card, SpellCard)])
            total_artifacts = len([card for card in self._cards
                                  if isinstance(card, ArtifactCard)])
            avg_cost = total_cost / total_cards
            status.update({'total_cards': total_cards,
                           'creatures': total_creatures,
                           'spells': total_spells,
                           'artifacts': total_artifacts,
                           'avg_cost': int(avg_cost)})
            return status
        except ZeroDivisionError:
            return status
