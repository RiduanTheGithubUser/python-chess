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
from chessPieces.blank import Blank

fenDecoded = []

def useFen(fen):
  for x in range(len(fen)):
    if fen[x]=='/':
      fenDecoded.append(Blank(2))
    elif fen[x]=='p':
      fenDecoded.append(Pawn(0))
    elif fen[x]=='n':
      fenDecoded.append(Knight(0))
    elif fen[x]=='b':
      fenDecoded.append(Bishop(0))
    elif fen[x]=='r':
      fenDecoded.append(Rook(0))
    elif fen[x]=='q':
      fenDecoded.append(Queen(0))
    elif fen[x]=='k':
      fenDecoded.append(King(0))
    elif fen[x]=='P':
      fenDecoded.append(Pawn(1))
    elif fen[x]=='N':
      fenDecoded.append(Knight(1))
    elif fen[x]=='B':
      fenDecoded.append(Bishop(1))
    elif fen[x]=='R':
      fenDecoded.append(Rook(1))
    elif fen[x]=='Q':
      fenDecoded.append(Queen(1))
    elif fen[x]=='K':
      fenDecoded.append(King(1))
    elif fen[x]=='1':
      fenDecoded.append(Blank(0))
    elif fen[x]=='2':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
    elif fen[x]=='3':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
    elif fen[x]=='4':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
    elif fen[x]=='5':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
    elif fen[x]=='6':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
    elif fen[x]=='7':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
    elif fen[x]=='8':
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))
      fenDecoded.append(Blank(0))

def getSymbol(type):
  if type.color==0:
    return type.bIcon
  elif type.color==1:
    return type.wIcon
  elif type.color==2:
    return type.hIcon

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
    self.chessFen = "rnbqkbnr/pppppppp/4p1/6/6/6/PPPPPPPP/RNBQKBNR"
  
  def printBoard(self, manager, chessfen):
    print(manager.ToMove + " to move\n\n")
    useFen(self.chessFen)
    result = ""
    for x in range(len(fenDecoded)):
      result += str(getSymbol(fenDecoded[x]))

    print(result)

class Pieces():
  def __init__(self, type):
    self.legalMoves = []
    self.type = type

  def initialize(self, type):
    # check what type is the piece
    pass


print('rnbqkbnr/pppppppp/4p1/6/6/6/PPPPPPPP/RNBQKBNR is the starting position')

chess = Chess()

board = Board()
board.printBoard(chess,board.chessFen)
