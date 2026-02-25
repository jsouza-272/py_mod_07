from .Deck import Deck
from ex0 import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from tools import CardGenerator

if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    cards = CardGenerator().generate_random_deck(3)
    deck = Deck()
    game_state = {"mana": 50}

    for card in cards:
        if "effect" in card:
            ll = ArtifactCard(**card)
        elif "attack" in card:
            ll = CreatureCard(**card)
        else:
            ll = SpellCard(**card)
        deck.add_card(ll)

    deck.shuffle()
    print("Deck stats:", deck.get_deck_status())

    print("\nDrawing and playing cards:")
    for i in range(len(deck.cards)):
        card = deck.draw_card()
        print(f"\nDrew: {card.name} ({card.type})")
        print("Play result:", card.play(game_state))

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")
