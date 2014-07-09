from Action import Action

class PlayAction(Action):
    def __init__(self, card_value):
        Action.__init__(self, 'play')
        self.card_value = card_value