from Khmer import Khmer, InvalidMoveError
from ConsolePlayer import ConsolePlayer

class ConsoleController:

    def run(self):
        khmer = Khmer.new_game()
        player_a = ConsolePlayer()
        player_b = ConsolePlayer()
        while not khmer.has_game_ended:
            if khmer.current_player == 'a':
                action = player_a.get_action(khmer)
            elif khmer.current_player == 'b':
                action = player_b.get_action(khmer)
            khmer.do(action)


if __name__ == '__main__':
    controller = ConsoleController()
    controller.run()