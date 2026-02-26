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
    game_state = {"mana": 15, "hand": [], "battlefield": []}

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
    for i in range(len(deck._cards)):
        card = deck.draw_card()
        game_state["hand"].append(card)
        print(f"\nDrew: {card._name} ({card._type})")
        print("Play result:", card.play(game_state))

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")
