from ex2 import EliteCard


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card:", ['play', 'get_card_info', 'is_playable'])
    print("- Combatable:", ['attack', 'defend', 'get_combat_stats'])
    print("- Magical:", ['cast_spell', 'channel_mana', 'get_magic_stats'])

    warrior = EliteCard('Arcane Warriror', 4, 'melee', 5, 10, 3, 8)
    Enemy = EliteCard('Enemy', 1, 'melee', 5, 10, 2, 10)
    Enemy1 = EliteCard('Enemy1', 1, 'melee', 5, 10, 2, 10)
    Enemy2 = EliteCard('Enemy2', 1, 'melee', 5, 10, 2, 10)
    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    print("Attack result:", warrior.attack(Enemy))
    print("Defense result:", warrior.defend(
        Enemy.attack(warrior)['damage']))

    print("\nMagic phase:")
    print("Spell cast:", warrior.cast_spell('Fireball', [Enemy1, Enemy2]))
    print("Mana channel:", warrior.channel_mana(3))

    print("\nMultiple interface implementation successful!")
