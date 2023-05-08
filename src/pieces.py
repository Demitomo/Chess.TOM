import pygame as py

window = py.display.set_mode((640, 640))

bgImg = py.image.load("Python/chess/GitHub/img/Board.png", "png")
bgImg = py.transform.scale(bgImg, (640, 640))

LastMove = None


class Piece:
    def __init__(self, color) -> None:
        self.color = color

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        pass

    def DisplayPiece(self, x, y):
        window.blit(self.image, (x * 80, y * 80))


class Pawn(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load(
            "Python/chess/GitHub/img/Wpawn.png" if self.color == "w" else "Python/chess/GitHub/img/Bpawn.png"
        )
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        global LastMove

        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        if (
                (y_loc - y_dest == 1 and self.color == "w")
                or (y_loc - y_dest == -1 and self.color == "b")
        ) and x_loc - x_dest == 0:
            if board[y_dest][x_dest] == "-":
                if self.PawnPromotion(y_dest):
                    board[y_dest][x_dest] = "Q" if self.color == "w" else "q"
                    board[y_loc][x_loc] = "-"
                else:
                    board[y_dest][x_dest] = "P" if self.color == "w" else "p"
                    board[y_loc][x_loc] = "-"
                if not checkingMoves: LastMove = None
                return board

        elif (
                (y_loc - y_dest == 2 and self.color == "w")
                or (y_loc - y_dest == -2 and self.color == "b")
        ) and x_loc - x_dest == 0:
            if (
                    board[y_dest][x_dest] == "-"
                    and board[y_dest + 1 if self.color == "w" else y_dest - 1][x_dest]
                    == "-"
            ):
                if y_loc == 1 or y_loc == 6:
                    board[y_dest][x_dest] = "P" if self.color == "w" else "p"
                    board[y_loc][x_loc] = "-"
                    if not checkingMoves: LastMove = x_dest
                    return board

        elif abs(x_loc - x_dest) == 1 and (
                (y_loc - y_dest == 1 and self.color == "w")
                or (y_loc - y_dest == -1 and self.color == "b")
        ):
            if (board[y_dest][x_dest].islower() and self.color == "w") or (
                    board[y_dest][x_dest].isupper() and self.color == "b"
            ):
                if self.PawnPromotion(y_dest):
                    board[y_dest][x_dest] = "Q" if self.color == "w" else "q"
                    board[y_loc][x_loc] = "-"
                else:
                    board[y_dest][x_dest] = "P" if self.color == "w" else "p"
                    board[y_loc][x_loc] = "-"
                if not checkingMoves: LastMove = None
                return board

            elif board[y_dest][x_dest] == "-" and x_dest == LastMove and ((y_loc == 3 and self.color == "w") or (y_loc == 4 and self.color == "b")):
                board[y_dest][x_dest] = "P" if self.color == "w" else "p"
                board[y_loc][x_loc] = "-"
                board[(y_dest + 1) if self.color == "w" else (y_dest - 1)][x_dest] = "-"
                if not checkingMoves: LastMove = None
                return board

        return False

    def PawnPromotion(self, y_dest):
        if y_dest == 0 or y_dest == 7:
            return True


class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load(
            "Python/chess/GitHub/img/Wknig.png" if self.color == "w" else "Python/chess/GitHub/img/Bknig.png"
        )
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        global LastMove

        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        if (abs(x_dest - x_loc) == 2 and abs(y_dest - y_loc) == 1) or (
                abs(x_dest - x_loc) == 1 and abs(y_dest - y_loc) == 2
        ):
            if (board[y_dest][x_dest].islower() and self.color == "b") or (
                    board[y_dest][x_dest].isupper() and self.color == "w"
            ):
                return False
            board[y_dest][x_dest] = "N" if self.color == "w" else "n"
            board[y_loc][x_loc] = "-"
            if not checkingMoves: LastMove = None
            return board

        return False


class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load(
            "Python/chess/GitHub/img/Wbish.png" if self.color == "w" else "Python/chess/GitHub/img/Bbish.png"
        )
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        global LastMove

        if loc == dest:
            return False

        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        if abs(x_dest - x_loc) == abs(y_dest - y_loc):
            if (board[y_dest][x_dest].islower() and self.color == "b") or (
                    board[y_dest][x_dest].isupper() and self.color == "w"
            ):
                return False
            if self.PathIsClear(board, loc, dest):
                board[y_dest][x_dest] = "B" if self.color == "w" else "b"
                board[y_loc][x_loc] = "-"
                if not checkingMoves: LastMove = None
                return board

        return False

    def PathIsClear(self, board, loc, dest):
        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        Xsteps = 1 if x_dest > x_loc else -1
        Ysteps = 1 if y_dest > y_loc else -1

        col, row = x_loc + Xsteps, y_loc + Ysteps

        while col != x_dest:
            if board[row][col] != "-":
                return False

            col += Xsteps
            row += Ysteps

        return True


class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load(
            "Python/chess/GitHub/img/Wrook.png" if self.color == "w" else "Python/chess/GitHub/img/Brook.png"
        )
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        global LastMove

        if loc == dest:
            return False

        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        if (abs(x_loc - x_dest) > 0 and abs(y_loc - y_dest) == 0) or (
                abs(x_loc - x_dest) == 0 and abs(y_loc - y_dest) > 0
        ):
            if (board[y_dest][x_dest].islower() and self.color == "b") or (
                    board[y_dest][x_dest].isupper() and self.color == "w"
            ):
                return False
            if self.PathIsClear(board, loc, dest):
                board[y_dest][x_dest] = "R" if self.color == "w" else "r"
                board[y_loc][x_loc] = "-"
                if not checkingMoves: LastMove = None
                return board

        return False

    def PathIsClear(self, board, loc, dest):
        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        stepsRow = 0 if y_loc == y_dest else 1 if y_loc < y_dest else -1
        stepsCol = 0 if x_loc == x_dest else 1 if x_loc < x_dest else -1

        row, col = y_loc + stepsRow, x_loc + stepsCol
        while (col != x_dest) if y_loc == y_dest else (row != y_dest):
            if board[row][col] != "-":
                return False

            row += stepsRow
            col += stepsCol

        return True


class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__(color)
        self.image = py.image.load(
            "Python/chess/GitHub/img/Wqueen.png" if self.color == "w" else "Python/chess/GitHub/img/Bqueen.png"
        )
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        global LastMove

        if loc == dest:
            return False

        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        if abs(x_dest - x_loc) == abs(y_dest - y_loc):
            if (board[y_dest][x_dest].islower() and self.color == "b") or (
                    board[y_dest][x_dest].isupper() and self.color == "w"
            ):
                return False
            if self.PathIsClear(board, loc, dest):
                board[y_dest][x_dest] = "Q" if self.color == "w" else "q"
                board[y_loc][x_loc] = "-"
                if not checkingMoves: LastMove = None
                return board

        elif (abs(x_loc - x_dest) > 0 and abs(y_loc - y_dest) == 0) or (
                abs(x_loc - x_dest) == 0 and abs(y_loc - y_dest) > 0
        ):
            if (board[y_dest][x_dest].islower() and self.color == "b") or (
                    board[y_dest][x_dest].isupper() and self.color == "w"
            ):
                return False
            if self.PathIsClear(board, loc, dest):
                board[y_dest][x_dest] = "Q" if self.color == "w" else "q"
                board[y_loc][x_loc] = "-"
                if not checkingMoves: LastMove = None
                return board

        return False

    def PathIsClear(self, board, loc, dest):
        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        stepsRow = 0 if y_loc == y_dest else 1 if y_loc < y_dest else -1
        stepsCol = 0 if x_loc == x_dest else 1 if x_loc < x_dest else -1

        row, col = y_loc + stepsRow, x_loc + stepsCol
        while (col != x_dest) if y_loc == y_dest else (row != y_dest):
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
        self.image = py.image.load(
            "Python/chess/GitHub/img/Wking.png" if self.color == "w" else "Python/chess/GitHub/img/Bking.png"
        )
        self.image = py.transform.scale(self.image, (80, 80))

    def IsMoveLegal(self, board, loc, dest, checkingMoves):
        global LastMove

        if loc == dest:
            return False

        x_loc, y_loc = loc[0], loc[1]
        x_dest, y_dest = dest[0], dest[1]

        if abs(x_loc - x_dest) <= 1 and abs(y_loc - y_dest) <= 1:
            if (board[y_dest][x_dest].islower() and self.color == "b") or (
                    board[y_dest][x_dest].isupper() and self.color == "w"
            ):
                return False
            if not checkingMoves: self.hasMoved = True
            board[y_dest][x_dest] = "K" if self.color == "w" else "k"
            board[y_loc][x_loc] = "-"
            if not checkingMoves: LastMove = None
            return board

        elif abs(x_loc - x_dest) == 2 and y_loc - y_dest == 0:
            if self.hasMoved:
                return False
            if self.PathIsClear(board, loc, dest):
                if not self.rookMoved[0] and x_dest - x_loc == 2:
                    if not checkingMoves: self.hasMoved = True
                    board[y_dest][x_dest] = "K" if self.color == "w" else "k"
                    board[y_loc][x_loc] = "-"
                    board[y_dest][x_dest - 1] = "R" if self.color == "w" else "r"
                    board[y_dest][x_dest + 1] = "-"
                    if not checkingMoves: LastMove = None
                    return board

                elif not self.rookMoved[1] and x_loc - x_dest == 2:
                    if not checkingMoves: self.hasMoved = True
                    board[y_dest][x_dest] = "K" if self.color == "w" else "k"
                    board[y_loc][x_loc] = "-"
                    board[y_dest][x_dest - 2] = "-"
                    board[y_dest][x_dest + 1] = "R" if self.color == "w" else "r"
                    if not checkingMoves: LastMove = None
                    return board

        return False

    def PathIsClear(self, board, loc, dest):
        x_pos = loc[1]
        x_loc, x_dest = loc[0], dest[0]

        step = 1 if x_dest == 6 else -1

        col = x_loc + step
        for _ in range(3 if x_dest != 6 else 2):
            if board[x_pos][col] != "-":
                return False
            col += step

        if (board[x_pos][col] == "R" and self.color == "w") or (
                board[x_pos][col] == "r" and self.color == "b"
        ):
            return True

        return False


if __name__ == "__main__":
    print("Vous ne pouvez pas lancer ce fichier directement")
    exit()