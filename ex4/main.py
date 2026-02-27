from .TournamentCard import TournamentCard
from . TournamentPlataform import TournamentPlataform

if __name__ == "__main__":
    card1 = TournamentCard(name='Fire Dragon', cost=6, rarity="Legendary",
                           attack=7, health=10, defense=3, rating=0)

    card2 = TournamentCard(name='Ice Wizard', cost=4, rarity="Uncommon",
                           attack=4, health=7, defense=1, rating=0)

    plataform = TournamentPlataform()
    print("\n=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    print(plataform.register_card(card1))
    print(plataform.register_card(card2))

    print("\nCreating tournament match...")
    print("Match result:", plataform.create_match("dragon_001", "wizard_001"))

    print("\nTournament Leaderboard:")
    i = 1
    for _ in plataform.get_leaderboard():
        print(f"{i}.", _)
        i += 1

    print("\nPlatform Report:")
    print(plataform.generate_tournament_report())

    print("\n== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

    # 100 matches
    # for i in range(100):
    #     c1, c2 = plataform.get_two_random_cards()
    #     plataform.create_match(c1._id, c2._id)
    #     c1.restore()
    #     c2.restore()
    # print("\nTournament Leaderboard:")
    # i = 1
    # for _ in plataform.get_leaderboard():
    #     print(f"{i}.", _)
    #     i += 1
