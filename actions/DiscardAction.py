from Action import Action

class DiscardAction(Action):
    def __init__(self):
        Action.__init__(self, 'discard')