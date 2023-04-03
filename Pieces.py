import pygame

Brook = pygame.image.load("./Python/Chess/V3/Images/Brook.png")
Brook = pygame.transform.scale(Brook, (80, 80))

Bknig = pygame.image.load("./Python/Chess/V3/Images/Bknig.png")
Bknig = pygame.transform.scale(Bknig, (80, 80))

Bbish = pygame.image.load("./Python/Chess/V3/Images/Bbish.png")
Bbish = pygame.transform.scale(Bbish, (80, 80))

Bqueen = pygame.image.load("./Python/Chess/V3/Images/Bqueen.png")
Bqueen = pygame.transform.scale(Bqueen, (80, 80))

Bking = pygame.image.load("./Python/Chess/V3/Images/Bking.png")
Bking = pygame.transform.scale(Bking, (80, 80))

Bpawn = pygame.image.load("./Python/Chess/V3/Images/Bpawn.png")
Bpawn = pygame.transform.scale(Bpawn, (80, 80))

Wrook = pygame.image.load("./Python/Chess/V3/Images/Wrook.png")
Wrook = pygame.transform.scale(Wrook, (80, 80))

Wknig = pygame.image.load("./Python/Chess/V3/Images/Wknig.png")
Wknig = pygame.transform.scale(Wknig, (80, 80))

Wbish = pygame.image.load("./Python/Chess/V3/Images/Wbish.png")
Wbish = pygame.transform.scale(Wbish, (80, 80))

Wqueen = pygame.image.load("./Python/Chess/V3/Images/Wqueen.png")
Wqueen = pygame.transform.scale(Wqueen, (80, 80))

Wking = pygame.image.load("./Python/Chess/V3/Images/Wking.png")
Wking = pygame.transform.scale(Wking, (80, 80))

Wpawn = pygame.image.load("./Python/Chess/V3/Images/Wpawn.png")
Wpawn = pygame.transform.scale(Wpawn, (80, 80))

Pieces = ["r", "n", "b", "q", "k", "p", "R", "N", "B", "Q", "K", "P"]
Images = [Brook, Bknig, Bbish, Bqueen, Bking, Bpawn, Wrook, Wknig, Wbish, Wqueen, Wking, Wpawn]

def InitBoard():
    board = []
    board.append("r")
    board.append("n")
    board.append("b")
    board.append("q")
    board.append("k")
    board.append("b")
    board.append("n")
    board.append("r")
    for _ in range(8):
        board.append("p")
    for _ in range(32):
        board.append("-")
    for _ in range(8):
        board.append("P")
    board.append("R")
    board.append("N")
    board.append("B")
    board.append("Q")
    board.append("K")
    board.append("B")
    board.append("N")
    board.append("R")
    return board