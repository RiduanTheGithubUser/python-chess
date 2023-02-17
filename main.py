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

from chessPieces.pawn import Pawn
from chessPieces.knight import Knight
from chessPieces.bishop import Bishop
from chessPieces.rook import Rook
from chessPieces.queen import Queen
from chessPieces.king import King

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

  def initialize(self, type):
    # check what type is the piece
    pass