class Queen():
    def __init__(self):
        self.canPromote = False
        self.moveCount = 0
        self.legalMoves = [move1:=['1','1'],move2:=['1','-1'],move3:=['-1','-1'],move4:=['-1','1'],move5:=['1','0'],move6:=['0','1'],move7:=['-1','0'],move8:=['0','-1']]
        self.needsKillMoves = False
        self.power = 100
        self.icon = "👑👩‍🦰"
    