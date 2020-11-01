from enum import Enum

class ChessArena:
    class Turn(Enum):
        WHITE = True
        BLACK = False

    def __init__(self):
        self._turn = self.Turn.WHITE

    def Act(self):
        print('Acting..')