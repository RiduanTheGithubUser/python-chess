class Bishop():
    def __init__(self):
        self.canPromote = False
        self.moveCount = 0
        self.legalMoves = [move1:=['1','1'],move2:=['1','-1'],move3:=['-1','-1'],move4:=['-1','1']]
        self.needsKillMoves = False
        self.power = 100
        self.icon = "☪"
    