import pygame

WPawn = pygame.image.load("../img/Wpawn.png")
WKnig = pygame.image.load("../img/Wknig.png")
WBish = pygame.image.load("../img/Wbish.png")
WRook = pygame.image.load("../img/Wrook.png")
WQueen = pygame.image.load("../img/Wqueen.png")
WKing = pygame.image.load("../img/Wking.png")
BPawn = pygame.image.load("../img/Bpawn.png")
BKnig = pygame.image.load("../img/Bknig.png")
BBish = pygame.image.load("../img/Bbish.png")
BRook = pygame.image.load("../img/Brook.png")
BQueen = pygame.image.load("../img/Bqueen.png")
BKing = pygame.image.load("../img/Bking.png")

WPawn = pygame.transform.scale(WPawn, (80, 80))
WKnig = pygame.transform.scale(WKnig, (80, 80))
WBish = pygame.transform.scale(WBish, (80, 80))
WRook = pygame.transform.scale(WRook, (80, 80))
WQueen = pygame.transform.scale(WQueen, (80, 80))
WKing = pygame.transform.scale(WKing, (80, 80))
BPawn = pygame.transform.scale(BPawn, (80, 80))
BKnig = pygame.transform.scale(BKnig, (80, 80))
BBish = pygame.transform.scale(BBish, (80, 80))
BRook = pygame.transform.scale(BRook, (80, 80))
BQueen = pygame.transform.scale(BQueen, (80, 80))
BKing = pygame.transform.scale(BKing, (80, 80))

bg = pygame.image.load("../img/Board.png")
bg = pygame.transform.scale(bg, (640, 640))

pieces = ["r", "n", "b", "q", "k", "p", "R", "N", "B", "Q", "K", "P"]
images = [BRook, BKnig, BBish, BQueen, BKing, BPawn, WRook, WKnig, WBish, WQueen, WKing, WPawn]

def BoardInit():
    board =[]
    board.append("r")
    board.append("n")
    board.append("b")
    board.append("q")
    board.append("k")
    board.append("b")
    board.append("n")
    board.append("r")
    for _ in range(8): board.append("p")
    for _ in range(32): board.append("-")
    for _ in range(8): board.append("P")
    board.append("R")
    board.append("N")
    board.append("B")
    board.append("Q")
    board.append("K")
    board.append("B")
    board.append("N")
    board.append("R")
    print(board)
    return board