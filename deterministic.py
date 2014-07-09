from itertools import imap, ifilter, product

class CardState:
    PLAYER_A = 1
    PLAYER_B = 2
    TABLE = 3
    DISCARD = 4

    @staticmethod
    def all():
        return [CardState.PLAYER_A, CardState.PLAYER_B, CardState.TABLE, CardState.DISCARD]

class GameState:

    CARDS = [1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,6]

    def __init__(self, game_state_data):
        self.data = game_state_data

    def player_a_sum(self):
        player_a_cards = self._cards_with_state(self, CardState.PLAYER_A)
        return sum(player_a_cards)

    def player_b_sum(self):
        player_b_cards = self._cards_with_state(self, CardState.PLAYER_B)
        return sum(player_b_cards)

    def table_sum(self):
        table_cards = self._cards_with_state(self, CardState.TABLE)
        return sum(table_cards)

    def _cards_with_state(self, card_state):
        is_state = lambda (card, state): state == CardState.PLAYER_B
        x = filter(is_state, zip(GameState.CARDS, self.data))
        return list(zip(*x)[0])

        ## TODO

    @staticmethod
    def all():
        game_states_data = product(CardState.all(), repeat=len(GameState.CARDS))
        is_valid = lambda game_state_data: game_state_data.count(CardState.DISCARD) >= 4
        valid_game_states_data = ifilter(is_valid, game_states_data)
        return imap(GameState, valid_game_states_data)

for game_state in GameState.all():
    print game_state.data, game_state.player_a_sum(), game_state_data.player_b_sum(), game_state_data.table_sum()

print 'done'