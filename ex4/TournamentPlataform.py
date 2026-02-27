from .TournamentCard import TournamentCard
import random


class TournamentPlataform():
    def __init__(self):
        self._cards_regitred: list[TournamentCard] = []
        self._ids_registred = [card._id for card in self._cards_regitred]
        self._match_played = 0

    def _update_ids(self) -> None:
        self._ids_registred = [card._id for card in self._cards_regitred]

    @staticmethod
    def _i_need_lambda(x: TournamentCard) -> int:
        return x._rating

    def register_card(self, card: TournamentCard) -> str:
        id = (card._name.split()[1] if len(card._name.split()) > 1
              else card._name.split()[0])
        id = id.lower()
        i = 1

        while f"{id}_{i:03}" in self._ids_registred:
            i += 1
        id = f"{id}_{i:03}"
        card._id = id
        self._cards_regitred.append(card)
        self._update_ids()

        interfaces = [cls.__name__ for cls in card.__class__.mro()[1:]
                      if cls.__name__ not in ("ABC", "object")]
        line1 = f"\n{card._name} (ID: {id}):"
        line2 = f"\n- Interfaces: {interfaces}"
        line3 = f"\n- Rating: {card._rating}"
        line4 = f"\n- Record: {card._wins}-{card._losses}"
        return line1 + line2 + line3 + line4

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if (card1_id in self._ids_registred
                and card2_id in self._ids_registred):
            card1 = self._cards_regitred[
                self._ids_registred.index(card1_id)]
            card2 = self._cards_regitred[
                self._ids_registred.index(card2_id)]
            print(card1, card2)
            while (card1.get_combat_status()['alive']
                    and card2.get_combat_status()['alive']):
                card1.attack(card2)
                card2.attack(card1)

            winner = (card1 if card1.get_combat_status()['alive'] else card2)
            winner.update_wins(1)
            winner.calculate_rating()

            loser = (card2 if card1.get_combat_status()['alive'] else card1)
            loser.update_losses(1)
            loser.calculate_rating()

            self._match_played += 1
            return {'winner': winner, 'loser': loser,
                    'winner_rating': winner._rating,
                    'loser_rating': loser._rating}
        return {'error': "Ids not found", 'ids avaiable': self._ids_registred}

    def get_leaderboard(self) -> list:
        helper_list = sorted(self._cards_regitred,
                             key=TournamentPlataform._i_need_lambda,
                             reverse=True)
        leaderboard = []
        for card in helper_list:
            info = card.get_rank_info()
            text = f"{info.get('name')} - Rating: \
{info.get('rating')} ({info.get('wins')}-{info.get('losses')})"
            leaderboard.append(text)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        return {'total_cards': len(self._cards_regitred),
                'matches_played': self._match_played,
                'avg_rating': sum([card._rating
                                   for card in self._cards_regitred]) / len(
                                       self._cards_regitred),
                'plataform_staus': 'active'
                }

    def get_two_random_cards(self) -> list:
        return random.sample(self._cards_regitred, 2)
