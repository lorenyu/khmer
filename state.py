from operator import attrgetter
from itertools import imap, ifilter, product, combinations, chain

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class Card:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

CARDS = map(Card, [1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,6])

class GameState:

    def __init__(self, player_a_cards, player_b_cards, table_cards, discard_cards):
        self.player_a_cards = set(player_a_cards)
        self.player_b_cards = set(player_b_cards)
        self.table_cards = list(table_cards)
        self.discard_cards = set(discard_cards)

    def player_a_sum(self):
        return sum(map(attrgetter('value'), self.player_a_cards))

    def player_b_sum(self):
        return sum(map(attrgetter('value'), self.player_b_cards))

    def table_sum(self):
        return sum(map(attrgetter('value'), self.table_cards))


# for game_state in GameState.all():
#     print game_state.player_a_cards, game_state.player_b_cards, game_state.table_cards, game_state.discard_cards

game_states = list(GameState.all())
print len(game_states)
print 'done'



























# class GameState:
#     # too inefficient =( 4^16 states is too many
#     @staticmethod
#     def all():
#         for discard_cards in combinations(CARDS, 4):
#             cards = set(CARDS) - set(discard_cards)
#             sixes_remaining = filter(lambda card: card.value == 6, sorted(cards))
#             for discard_sixes in [sixes_remaining[:n] for n in range(len(sixes_remaining) + 1)]:
#                 discard_cards = set(discard_cards) | set(discard_sixes)
#                 cards = cards - set(discard_sixes)
#                 for player_a_cards in powerset(cards):
#                     cards = cards - set(player_a_cards)
#                     for player_b_cards in powerset(cards):
#                         table_cards = cards - set(player_b_cards)
#                         yield GameState(player_a_cards, player_b_cards, table_cards, discard_cards)