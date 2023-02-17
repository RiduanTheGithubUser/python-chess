#----------------------------------------------
#                      A
# /-----| |  |       |------- |------- |-------
#| /----| |  |       |  /-\ | |  ____| |  ____|
#|        |  ------| |  \_/ | |  \____ |  \____
#|        |  ____  | |  ____| |____  | |____  |
#| \----| |  |  |  | |  |___  ___/   | ___/   |
# \-----| |__|  |__| |______| |______| |______|
#                     game
#----------------------------------------------

class Chess():
  def __init__(self):
    self.ToMove = "White"

  def move():
    # lets pieces move in their legal move table
    pass

  def promotion():
    # self-explanitory
    pass

class Board():
  def __init__(self):
    # default chess layout
    self.chessLayout = ""
  
  def printBoard(self):
    # print the board however you want
    pass


class Pieces():
  def __init__(self, type):
    self.legalMoves = []
    self.type = type
  
  def legalizeMoves(self):
    # here you can add to the legal moves
    pass