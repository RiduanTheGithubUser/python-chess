class Rook():
    def __init__(self):
        self.canPromote = False
        self.moveCount = 0
        self.legalMoves = [move1:=['1','0'],move2:=['0','1'],move3:=['-1','0'],move4:=['0','-1']]
        self.needsKillMoves = False
        self.power = 100
        self.icon = "🏰"
    