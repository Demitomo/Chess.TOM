import pygame as py

window = py.display.set_mode((640, 640))

bgImg = py.image.load("../img/Board.png")
bgImg = py.transform.scale(bgImg, (640, 640))

LastMove = None

class Piece:
    def __init__(self, color) -> None:
        self.color = color
    
    def IsMoveLegal(self):
        pass
    
    def DisplayPiece(self, x, y):
        window.blit(self.image, (x * 80, y * 80))


class Pawn(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load("../img/Wpawn.png" if self.color == "w" else "../img/Bpawn.png")
        self.image = py.transform.scale(self.image, (80, 80))
        

        self.image = py.transform.scale(self.image, (80, 80))
    def IsMoveLegal(self, board, loc, dest):
        global LastMove

        Xloc = loc[0]
        Yloc = loc[1]
        Xdest = dest[0]
        Ydest = dest[1]

        if ((Yloc - Ydest == 1 and self.color == "w") or (Yloc - Ydest == -1 and self.color == "b")) and Xloc - Xdest == 0:
            if board[Ydest][Xdest] == "-":
                if self.PawnPromotion(Ydest):
                    board[Ydest][Xdest] = "Q" if self.color == "w" else "q"
                    board[Yloc][Xloc] = "-"
                else:
                    board[Ydest][Xdest] = "P" if self.color == "w" else "p"
                    board[Yloc][Xloc] = "-"
                LastMove = None
                return board
        
        elif ((Yloc - Ydest == 2 and self.color == "w") or (Yloc - Ydest == -2 and self.color == "b")) and Xloc - Xdest == 0:
            if board[Ydest][Xdest] == "-" and board[Ydest -1 if self.color == "w" else Ydest + 1][Xdest] == "-":
                if Yloc == 1 or Yloc == 6:
                    board[Ydest][Xdest] = "P" if self.color == "w" else "p"
                    board[Yloc][Xloc] = "-"
                    LastMove = Xdest
                    return board
        
        elif abs(Xloc - Xdest) == 1 and ((Yloc - Ydest == 1 and self.color == "w") or (Yloc - Ydest == -1 and self.color == "b")):
            if (board[Ydest][Xdest].islower() and self.color == "w") or (board[Ydest][Xdest].isupper() and self.color == "b"):
                if self.PawnPromotion(Ydest):
                    board[Ydest][Xdest] = "Q" if self.color == "w" else "q"
                    board[Yloc][Xloc] = "-"
                else:
                    board[Ydest][Xdest] = "P" if self.color == "w" else "p"
                    board[Yloc][Xloc] = "-"
                LastMove = None
                return board

            elif board[Ydest][Xdest] == "-" and Xdest == LastMove:
                board[Ydest][Xdest] = "P" if self.color == "w" else "p"
                board[Yloc][Xloc] = "-"
                board[(Ydest + 1) if self.color == "w" else (Ydest - 1)][Xdest] = "-"
                LastMove = None
                return board
        
        return False
    
    def PawnPromotion(self, Ydest):
        if Ydest == 0 or Ydest == 7:
            return True


class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load("../img/Wknig.png" if self.color == "w" else "../img/Bknig.png")
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest):
        global LastMove

        Xloc = loc[0]
        Yloc = loc[1]
        Xdest = dest[0]
        Ydest = dest[1]


        if (abs(Xdest - Xloc) == 2 and abs(Ydest - Yloc) == 1) or (abs(Xdest - Xloc) == 1 and abs(Ydest - Yloc) == 2):
            if (board[Ydest][Xdest].islower() and self.color == "b") or (board[Ydest][Xdest].isupper() and self.color == "w"): return False
            board[Ydest][Xdest] = "N" if self.color == "w" else "n"
            board[Yloc][Xloc] = "-"
            LastMove = None
            return board

        return False


class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load("../img/Wbish.png" if self.color == "w" else "../img/Bbish.png")
        self.image = py.transform.scale(self.image, (80, 80))
        

    def IsMoveLegal(self, board, loc, dest):
        global LastMove

        if loc == dest: return False

        Xloc, Yloc = loc[0], loc[1]
        Xdest, Ydest = dest[0], dest[1]

        if abs(Xdest - Xloc) == abs(Ydest - Yloc):
            if (board[Ydest][Xdest].islower() and self.color == "b") or (board[Ydest][Xdest].isupper() and self.color == "w"): return False
            if self.PathIsClear(board, loc, dest):
                board[Ydest][Xdest] = "B" if self.color == "w" else "b"
                board[Yloc][Xloc] = "-"
                LastMove = None
                return board

        return False
    
    def PathIsClear(self, board, loc, dest):
        Xloc, Yloc = loc[0], loc[1]
        Xdest, Ydest = dest[0], dest[1]

        Xsteps = 1 if Xdest > Xloc else -1
        Ysteps = 1 if Ydest > Yloc else -1

        col, row = Xloc + Xsteps, Yloc + Ysteps

        while col != Xdest:
            if board[row][col] != "-": return False

            col += Xsteps
            row += Ysteps
        
        return True


class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load("../img/Wrook.png" if self.color == "w" else "../img/Brook.png")
        self.image = py.transform.scale(self.image, (80, 80))
        

    def IsMoveLegal(self, board, loc, dest):
        global LastMove

        if loc == dest: return False

        Xloc, Yloc = loc[0], loc[1]
        Xdest, Ydest = dest[0], dest[1]

        if (abs(Xloc - Xdest) > 0 and abs(Yloc - Ydest) == 0) or (abs(Xloc - Xdest) == 0 and abs(Yloc - Ydest) > 0):
            if (board[Ydest][Xdest].islower() and self.color == "b") or (board[Ydest][Xdest].isupper() and self.color == "w"): return False
            if self.PathIsClear(board, loc, dest):
                board[Ydest][Xdest] = "R" if self.color == "w" else "r"
                board[Yloc][Xloc] = "-"
                LastMove = None
                return board
        
        return False
    
    def PathIsClear(self, board, loc, dest):
        Xloc, Yloc = loc[0], loc[1]
        Xdest, Ydest = dest[0], dest[1]

        stepsRow = 0 if Yloc == Ydest else 1 if Yloc < Ydest else -1
        stepsCol = 0 if Xloc == Xdest else 1 if Xloc < Xdest else -1

        row, col = Yloc + stepsRow, Xloc + stepsCol
        while (col != Xdest) if Yloc == Ydest else (row != Ydest):
            if board[row][col] != "-":
                return False
            
            row += stepsRow
            col += stepsCol
        
        return True


class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load("../img/Wqueen.png" if self.color == "w" else "../img/Bqueen.png")
        self.image = py.transform.scale(self.image, (80, 80))
        

    def IsMoveLegal(self, board, loc, dest):
        global LastMove

        if loc == dest: return False

        Xloc, Yloc = loc[0], loc[1]
        Xdest, Ydest = dest[0], dest[1]

        if abs(Xdest - Xloc) == abs(Ydest - Yloc):
            if (board[Ydest][Xdest].islower() and self.color == "b") or (board[Ydest][Xdest].isupper() and self.color == "w"): return False
            if self.PathIsClear(board, loc, dest):
                board[Ydest][Xdest] = "Q" if self.color == "w" else "q"
                board[Yloc][Xloc] = "-"
                LastMove = None
                return board

        elif (abs(Xloc - Xdest) > 0 and abs(Yloc - Ydest) == 0) or (abs(Xloc - Xdest) == 0 and abs(Yloc - Ydest) > 0):
            if (board[Ydest][Xdest].islower() and self.color == "b") or (board[Ydest][Xdest].isupper() and self.color == "w"): return False
            if self.PathIsClear(board, loc, dest):
                board[Ydest][Xdest] = "Q" if self.color == "w" else "q"
                board[Yloc][Xloc] = "-"
                LastMove = None
                return board
        
        return False
    
    def PathIsClear(self, board, loc, dest):
        Xloc, Yloc = loc[0], loc[1]
        Xdest, Ydest = dest[0], dest[1]

        stepsRow = 0 if Yloc == Ydest else 1 if Yloc < Ydest else -1
        stepsCol = 0 if Xloc == Xdest else 1 if Xloc < Xdest else -1

        row, col = Yloc + stepsRow, Xloc + stepsCol
        while (col != Xdest) if Yloc == Ydest else (row != Ydest):
            if board[row][col] != "-":
                return False
            
            row += stepsRow
            col += stepsCol
        
        return True



class King(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.hasMoved = False
        self.rookMoved = [False, False]
        self.image = py.image.load("../img/Wking.png" if self.color == "w" else "../img/Bking.png")
        self.image = py.transform.scale(self.image, (80, 80))
        

    def IsMoveLegal(self, board, loc, dest):
        global LastMove

        if loc == dest: return False

        Xloc = loc[0]
        Yloc = loc[1]
        Xdest = dest[0]
        Ydest = dest[1]

        if abs(Xloc - Xdest) <= 1 and abs(Yloc - Ydest) <= 1:
            if (board[Ydest][Xdest].islower() and self.color == "b") or (board[Ydest][Xdest].isupper() and self.color == "w"): return False
            self.hasMoved = True
            board[Ydest][Xdest] = "K" if self.color == "w" else "k"
            board[Yloc][Xloc] = "-"
            LastMove = None
            return board
        
        elif abs(Xloc - Xdest) == 2 and Yloc - Ydest == 0:
            if self.hasMoved: return False
            if self.PathIsClear(board, loc, dest):
                if not self.rookMoved[0] and Xdest - Xloc == 2:
                    self.hasMoved = True
                    board[Ydest][Xdest] = "K" if self.color == "w" else "k"
                    board[Yloc][Xloc] = "-"
                    board[Ydest][Xdest - 1] = "R" if self.color == "w" else "r"
                    board[Ydest][Xdest + 1] = "-"
                    LastMove = None
                    return board

                elif not self.rookMoved[1] and Xloc - Xdest == 2:
                    self.hasMoved = True
                    board[Ydest][Xdest] = "K" if self.color == "w" else "k"
                    board[Yloc][Xloc] = "-"
                    board[Ydest][Xdest - 2] = "-"
                    board[Ydest][Xdest + 1] = "R" if self.color == "w" else "r"
                    LastMove = None
                    return board
        
        return False
    
    def PathIsClear(self, board, loc, dest):
        Ypos = loc[1]
        Xloc, Xdest = loc[0], dest[0]

        step = 1 if Xdest == 6 else -1

        col = Xloc + step
        for _ in range(3 if Xdest != 6 else 2):
            if board[Ypos][col] != "-": return False
            col += step
        
        if (board[Ypos][col] == "R" and self.color == "w") or (board[Ypos][col] == "r" and self.color == "b"):
            return True

        return False