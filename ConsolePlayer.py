from actions import *

class ConsolePlayer:

    def get_action(self, game):
        self.render_game(game)
        while True:
            action_name = raw_input('What is your move? ')

            if action_name == 'knock':
                return KnockAction()

            elif action_name == 'draw':
                return DrawAction()

            elif action_name == 'discard':
                return DiscardAction()

            elif action_name.startswith('play'):
                action_name, card_value = action_name.split()[:2]
                card_value = int(card_value)
                return PlayAction(card_value)

            print '{} is not a valid move'.format(action_name)

    def render_game(self, game):
        print 'You: ', sorted(game.current_player_cards)
        print 'Table: ', game.table_cards
        print 'Opponent has {} cards'.format(len(game.other_player_cards))