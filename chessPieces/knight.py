class Knight():
    def __init__(self, color):
        self.canPromote = False
        self.moveCount = 0
        self.legalMoves = [move1:=['2','-1'],move2:=['2','1'],move3:=['1','-2'],move4:=['1','2'],move5:=['-1','-2'],move6:=['1','2']]
        self.needsKillMoves = False
        self.power = 1
        self.bIcon = "♞"
        self.wIcon = "♘"
        self.color = color