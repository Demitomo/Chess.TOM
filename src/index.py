from pieces import *


class Board:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
        self.selectedPiece = None
        self.checkMate = False
        self.whiteToPlay = True
        self.running = True
        self.fps = py.time.Clock()
        self.possibleMoves = []

    def PrintBoard(self):
        for y in range(8):
            for x in range(8):
                if self.board[y][x] == "-":
                    continue

                Pieces[self.board[y][x]].DisplayPiece(x, y)

    def Events(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = False

            elif event.type == py.MOUSEBUTTONDOWN:
                if event.button != 1:
                    return

                pos = py.mouse.get_pos()
                x, y = int(pos[0] / 80), int(pos[1] / 80)

                if self.selectedPiece is None:
                    if self.board[y][x] == "-":
                        return
                    if (self.board[y][x].islower() and self.whiteToPlay) or (
                            self.board[y][x].isupper() and not self.whiteToPlay
                    ):
                        return

                    self.selectedPiece = [x, y, self.board[y][x]]
                    # Create a list of all possible moves
                    # by calling the IsMoveLegal function
                    # for each position of the selected piece

                    self.possibleMoves.clear()
                    for i in range(8):
                        for j in range(8):
                            temp_board = [row[:] for row in self.board]
                            if Pieces[self.selectedPiece[2]].IsMoveLegal(
                                    temp_board, self.selectedPiece[:2], [i, j], True) is not False:
                                self.possibleMoves.append([i, j])

                else:
                    dest = [x, y]
                    if dest == self.selectedPiece[:2]:
                        self.selectedPiece = None
                        self.possibleMoves.clear()
                        return

                    Move = Pieces[self.selectedPiece[2]].IsMoveLegal(
                        self.board, self.selectedPiece[:2], dest, False
                    )

                    if not Move:
                        return
                    else:
                        self.possibleMoves.clear()
                        self.whiteToPlay = not self.whiteToPlay
                        self.board = Move

                        if self.selectedPiece[2] == "r":
                            if self.selectedPiece[:2] == [0, 0]:
                                Pieces["k"].rookMoved[1] = True
                            elif self.selectedPiece[:2] == [7, 0]:
                                Pieces["k"].rookMoved[0] = True

                        elif self.selectedPiece[2] == "R":
                            if self.selectedPiece[:2] == [0, 7]:
                                Pieces["K"].rookMoved[1] = True
                            elif self.selectedPiece[:2] == [7, 7]:
                                Pieces["K"].rookMoved[0] = True

                        self.selectedPiece = None

    def Display(self):
        self.screen.fill("black")
        self.screen.blit(bgImg, (0, 0))

        if self.selectedPiece is not None:
            rect = py.rect.Rect(
                self.selectedPiece[0] * 80, self.selectedPiece[1] * 80, 80, 80
            )
            py.draw.rect(self.screen, "yellow", rect)

        self.PrintBoard()

        for move in self.possibleMoves:
            py.draw.circle(self.screen, "darkgray", (move[0] * 80 + 40, move[1] * 80 + 40), 10)

        py.display.flip()

    def Run(self):
        while self.running:
            self.Events()
            self.Display()
            self.fps.tick(60)


Pieces = {
    "p": Pawn("b"),
    "n": Knight("b"),
    "b": Bishop("b"),
    "r": Rook("b"),
    "q": Queen("b"),
    "k": King("b"),
    "P": Pawn("w"),
    "N": Knight("w"),
    "B": Bishop("w"),
    "R": Rook("w"),
    "Q": Queen("w"),
    "K": King("w"),
}


def Main():
    py.display.set_caption("Chess.tom")
    py.display.set_icon(py.image.load("../img/Icon.png"))

    Game = Board(window)
    Game.Run()


if __name__ == "__main__":
    Main()