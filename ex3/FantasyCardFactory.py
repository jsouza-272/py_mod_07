from .Cardfactory import CardFactory
import random
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard, Deck


class FantasyCardFactory(CardFactory):
    _creatures = [
            {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
                "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2, "rarity": "Common",
                "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4, "rarity": "Rare",
                "attack": 3, "health": 4},
            {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon",
                "attack": 4, "health": 2},
            {"name": "Stone Golem", "cost": 6, "rarity": "Rare", "attack": 5,
                "health": 8},
            {"name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon",
                "attack": 5, "health": 2},
            {"name": "Healing Angel", "cost": 4, "rarity": "Rare", "attack": 2,
                "health": 6},
            {"name": "Forest Sprite", "cost": 1, "rarity": "Common",
                "attack": 1, "health": 1}
        ]

    _spells = [
        {"name": "Lightning Bolt", "cost": 3, "rarity": "Common",
            "effect_type": "damage"},
        {"name": "Healing Potion", "cost": 2, "rarity": "Common",
            "effect_type": "heal"},
        {"name": "Fireball", "cost": 4, "rarity": "Uncommon",
            "effect_type": "damage"},
        {"name": "Shield Spell", "cost": 1, "rarity": "Common",
            "effect_type": "buff"},
        {"name": "Meteor", "cost": 8, "rarity": "Legendary",
            "effect_type": "damage"},
        {"name": "Ice Shard", "cost": 2, "rarity": "Common",
            "effect_type": "damage"},
        {"name": "Divine Light", "cost": 5, "rarity": "Rare",
            "effect_type": "heal"},
        {"name": "Magic Missile", "cost": 1, "rarity": "Common",
            "effect_type": "damage"}
    ]

    _artifacts = [
        {"name": "Mana Crystal", "cost": 2, "rarity": "Common",
            "durability": 5, "effect": "Permanent: +1 mana per turn"},
        {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon",
            "durability": 3,
            "effect": "Permanent: +2 attack to equipped creature"},
        {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare",
            "durability": 4,
            "effect": "Permanent: Draw an extra card each turn"},
        {"name": "Shield of Defense", "cost": 5, "rarity": "Rare",
            "durability": 6,
            "effect": "Permanent: +3 health to all friendly creatures"},
        {"name": "Crown of Kings", "cost": 7, "rarity": "Legendary",
            "durability": 8,
            "effect": "Permanent: +1 cost reduction to all cards"},
        {"name": "Boots of Speed", "cost": 2, "rarity": "Uncommon",
            "durability": 2, "effect": "Permanent: Cards cost 1 less mana"},
        {"name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon",
            "durability": 3, "effect": "Permanent: Creatures have stealth"},
        {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary",
            "durability": 7, "effect": "Permanent: +1 spell damage"}
    ]

    _all = _artifacts + _creatures + _spells

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in (creature.get('name')
                             for creature in self._creatures):
            creature = [creature for creature in self._creatures
                        if name_or_power == creature.get('name')]
            return CreatureCard(**creature[0])
        elif name_or_power in (creature.get('attack')
                               for creature in self._creatures):
            creature = [creature for creature in self._creatures
                        if name_or_power == creature.get('attack')]
            return CreatureCard(**random.choice(creature))
        elif name_or_power is None:
            return CreatureCard(**random.choice(self._creatures))
        else:
            if isinstance(name_or_power, str):
                print(f'Creature "{name_or_power}" not exist.')
            else:
                print(f'Creature with power {name_or_power} not exist.')
            print('Creating a random creature...')
            return CreatureCard(**random.choice(self._creatures))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in (spell.get('name')
                             for spell in self._spells):
            spell = [spell for spell in self._spells
                     if name_or_power == spell.get('name')]
            return SpellCard(**spell[0])
        elif name_or_power in (spell.get('cost')
                               for spell in self._spells):
            spell = [spell for spell in self._spells
                     if name_or_power == spell.get('cost')]
            return SpellCard(**random.choice(spell))
        elif name_or_power is None:
            return SpellCard(**random.choice(FantasyCardFactory._spells))
        else:
            if isinstance(name_or_power, str):
                print(f'Spell "{name_or_power}" not exist.')
            else:
                print(f'Spell with power {name_or_power} not exist.')
            print('Creating a random spell...')
            return SpellCard(**random.choice(self._spells))

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power in (artifact.get('name')
                             for artifact in self._artifacts):
            artifact = [artifact for artifact in self._artifacts
                        if name_or_power == artifact.get('name')]
            return ArtifactCard(**artifact[0])
        elif name_or_power is None:
            return ArtifactCard(**random.choice(self._artifacts))
        else:
            if isinstance(name_or_power, str):
                print(f'Artifact {name_or_power} not exist.')
            else:
                print('Artifact has no power.')
            print('Creating a random artifact...')
            return ArtifactCard(**random.choice(self._artifacts))

    def create_themed_deck(self, size: int) -> dict:
        if size < 2 or size > len(self._all):
            print(f'Invalid deck size: {size} (max 20, min 10)')
            return {}
        deck = Deck()
        cards = random.sample(self._all, k=size)
        for card in cards:
            if "attack" in card:
                deck.add_card(CreatureCard(**card))
            elif "effect" in card:
                deck.add_card(ArtifactCard(**card))
            else:
                deck.add_card(SpellCard(**card))
        return {'deck': deck}

    def get_supported_types(self) -> dict:
        return {'creatures': [creature.get('name')
                              for creature in self._creatures],
                'spells': [spell.get('name')
                           for spell in self._spells],
                'artifacts': [artifact.get('name')
                              for artifact in self._artifacts]}
