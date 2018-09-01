from Card import Card
from random import shuffle
from operator import attrgetter

CARDS = map(Card, [1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,6])

class BaseError(Exception):
    pass

class InvalidMoveError(BaseError):
    pass

class Khmer:

    # player_a_cards: list of Card
    # player_b_cards: list of Card
    # table_cards: list of Card
    # discard_cards: list of Card
    # current_player: 'a' | 'b'
    def __init__(self, player_a_cards, player_b_cards, table_cards, discard_cards, current_player):
        self.player_a_cards = set(player_a_cards)
        self.player_b_cards = set(player_b_cards)
        self.table_cards = list(table_cards)
        self.discard_cards = set(discard_cards)
        self.current_player = current_player
        self.has_game_ended = False
        self.winner = None

    @property
    def player_a_sum(self):
        return sum(map(attrgetter('value'), self.player_a_cards))

    @property
    def player_b_sum(self):
        return sum(map(attrgetter('value'), self.player_b_cards))

    @property
    def current_player_sum(self):
        return sum(map(attrgetter('value'), self.current_player_cards))

    @property
    def other_player_sum(self):
        return sum(map(attrgetter('value'), self.other_player_cards))

    @property
    def table_sum(self):
        return sum(map(attrgetter('value'), self.table_cards))

    @property
    def current_player_cards(self):
        if self.current_player == 'a':
            return self.player_a_cards
        elif self.current_player == 'b':
            return self.player_b_cards

    @property
    def other_player_cards(self):
        if self.current_player == 'a':
            return self.player_b_cards
        elif self.current_player == 'b':
            return self.player_a_cards

    @property
    def other_player(self):
        if self.current_player == 'a':
            return 'b'
        elif self.current_player == 'b':
            return 'a'

    @property
    def can_draw(self):
        return len(self.table_cards) > 0

    def knock(self):
        player_sum = self.current_player_sum
        other_player_sum = self.other_player_sum
        table_sum = self.table_sum

        if player_sum <= table_sum and player_sum > other_player_sum:
            self.winner = self.current_player
        else:
            self.winner = self.other_player

        self.has_game_ended = True

    def draw(self):
        if len(self.table_cards) <= 0:
            raise InvalidMoveError('Cannot draw. No cards on table.')

        self.current_player_cards.add(self.table_cards.pop())
        self.current_player = self.other_player

    def discard(self):
        sixes = filter(lambda card: card.value == 6, self.current_player_cards)

        if len(sixes) <= 0:
            raise InvalidMoveError('Cannot discard. No sixes in hand.')

        six = sixes[0]
        self.current_player_cards.remove(six)
        self.discard_cards.add(six)
        self.current_player = self.other_player

    def play(self, card_value):
        matching_cards = filter(lambda card: card.value == card_value, self.current_player_cards)

        if len(matching_cards) <= 0:
            raise InvalidMoveError("Cannot play card. Card not in player's hand.")

        card = matching_cards[0]
        self.current_player_cards.remove(card)
        self.table_cards.append(card)
        self.current_player = self.other_player

    def do(self, action):
        self.validate(action)

        if action.name == 'draw':
            self.draw()

        elif action.name == 'discard':
            self.discard()

        elif action.name == 'knock':
            self.knock()

        elif action.name == 'play':
            self.play(action.card_value)

    def validate(self, action):
        if action.name not in ['discard', 'draw', 'knock', 'play']:
            raise InvalidMoveError("Invalid move {}".format(action.name))

        if action.name == 'draw':
            if len(self.table_cards) <= 0:
                raise InvalidMoveError('Cannot draw. No cards on table.')

        elif action.name == 'discard':
            sixes = filter(lambda card: card.value == 6, self.current_player_cards)
            if len(sixes) <= 0:
                raise InvalidMoveError('Cannot discard. No sixes in hand.')

        elif action.name == 'play':
            matching_cards = filter(lambda card: card.value == action.card_value, self.current_player_cards)
            if len(matching_cards) <= 0:
                raise InvalidMoveError("Cannot play card. Card not in player's hand.")

    def is_valid(self, action):
        try:
            self.validate(action)
        except InvalidMoveError, e:
            return False
        return True

    @staticmethod
    def new_game():
        cards = list(CARDS)
        shuffle(cards)
        return Khmer(cards[0:6], cards[6:12], [], cards[12:16], 'a')