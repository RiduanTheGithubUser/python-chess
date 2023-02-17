class Pawn():
    def __init__(self):
        self.canPromote = False
        self.moveCount = 0
        self.legalMoves = [move1:=['1','0'],kill1:=['1','-1'],kill2:=['1','1']]
        self.needsKillMoves = True
        self.power = 1
        self.icon = "♟"
    