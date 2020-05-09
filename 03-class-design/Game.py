class Game:
    """ Represents main Game class"""

    def __init__(self):
        self.state = 'Ready'
        self.score = 0
        self.objects_found = []
        self.keys = {}
        self.messages = []
        self.player = None

    def play(self):
        self.new_attribute = 1
