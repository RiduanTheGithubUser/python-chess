class King():
    def __init__(self, color):
        self.canPromote = False
        self.moveCount = 0
        self.legalMoves = [move1:=['1','1'],move2:=['1','-1'],move3:=['1','0'],move4:=['0','1'],move5:=['0','-1'],move6:=['-1','-1'],move7:=['-1','1'],move8:=['-1','0']]
        self.needsKillMoves = False
        self.power = 1
        self.bIcon = "♚"
        self.wIcon = "♔"
        self.color = color