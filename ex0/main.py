from .CreatureCard import CreatureCard
from tools.card_generator import CardGenerator


if __name__ == "__main__":
    card1 = CreatureCard(**CardGenerator().get_creature("Fire Dragon"))
    card2 = CreatureCard(**CardGenerator().get_creature("Goblin Warrior"))
    player1 = {"mana": 6}
    player2 = {"mana": 3}

    print("\n=== DataDeck Card Foundation ===")
    print("\nCreatureCard Info:")
    print(card1.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", card1.is_playable(player1["mana"]))
    print("Play result", card1.play(player1))

    print(f"\nFire Dragon attacks {card2.name}:")
    print("Attack result:", card1.attack_target(card2))

    print("\nTesting insufficient mana (3 avaiable):")
    print("Playable:", card1.is_playable(player2["mana"]))

    print("\nAbstract pattern successfully demonstrated!")
