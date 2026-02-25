from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
import random


class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card_name)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) > 0:
            return self.cards.pop(0)

    def get_deck_status(self) -> dict:
        status = {'total_card': 0,
                  'creatures': 0,
                  'spells': 0,
                  'artifacts': 0,
                  'avg_cost': 0}
        try:
            total_cost = sum([card.cost
                              for card in self.cards])
            total_cards = len(self.cards)
            total_creatures = len([card for card in self.cards
                                   if isinstance(card, CreatureCard)])
            total_spells = len([card for card in self.cards
                                if isinstance(card, SpellCard)])
            total_artifacts = len([card for card in self.cards
                                  if isinstance(card, ArtifactCard)])
            avg_cost = total_cost / total_cards
            status.update({'total_card': total_cards,
                           'creatures': total_creatures,
                           'spells': total_spells,
                           'artifacts': total_artifacts,
                           'avg_cost': int(avg_cost)})
            return status
        except ZeroDivisionError:
            return status
