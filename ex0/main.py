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
    print("Play result", card1.play(player1))

    print(f"\nFire Dragon attacks {card2.name}:")
    print("Attack result:", card1.attack_target(card2))

    print("\nTesting insufficient mana (3 avaiable):")
    play_result = card1.play(player2)
    print(f"{play_result if play_result is not None else ''}")

    print("Abstract pattern successfully demonstrated!")
