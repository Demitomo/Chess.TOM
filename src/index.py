import pygame
from pieces import *
from checks import *

class Board:
    def __init__(self, screen, backgroundImg):
        self.screen = screen
        self.board = BoardInit()
        self.bg = backgroundImg
        self.area = pygame.Rect(700, 700, 80, 80)
        self.running = True
        self.chose = False
        self.WhiteToPlay = True
        self.fps = pygame.time.Clock()
    
    def Events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                MousePos = pygame.mouse.get_pos()

                if 30 <= MousePos[0] <= 670 and 30 <= MousePos[1] <= 670:
                    x = int((MousePos[0] - 30) / 80)
                    y = int((MousePos[1] - 30) / 80)
                    loc = y * 8 + x

                    if not self.chose:
                        whitePiece = self.WhiteToPlay and self.board[loc].isupper()
                        blackPiece = not self.WhiteToPlay and self.board[loc].islower()

                        if whitePiece or blackPiece:
                            self.piece = self.board[loc]
                            self.loc = loc
                            self.area = pygame.Rect(x * 80 + 30, y * 80 + 30, 80, 80)
                            self.chose = True

                    else:
                        if loc == self.loc:
                            self.area = pygame.Rect(700, 700, 80, 80)
                            self.chose = False
                        else:
                            if self.piece.lower() == "p": posbs = CheckPawn(self.loc, self.board)
                            elif self.piece.lower() == "n": posbs = CheckKnight(self.loc, self.board)
                            elif self.piece.lower() == "b": posbs = CheckBishop(self.loc, self.board)
                            elif self.piece.lower() == "r": posbs = CheckRook(self.loc, self.board)
                            elif self.piece.lower() == "q": posbs = CheckQueen(self.loc, self.board)
                            elif self.piece.lower() == "k": posbs = CheckKing(self.loc, self.board)


                            if loc in posbs:
                                self.board[self.loc] = "-"
                                self.board[loc] = self.piece
                                self.area = pygame.Rect(700, 700, 80, 80)
                                self.chose = False
                                if self.WhiteToPlay: self.WhiteToPlay = False
                                else: self.WhiteToPlay = True


    def Display(self):
        self.screen.fill("black")
        self.screen.blit(self.bg, (30, 30))
        pygame.draw.rect(self.screen, "yellow", self.area)

        Stops = [0, 8, 16, 24, 32, 40, 48, 56]
        for i, vali in enumerate(self.board):
            if vali == "-":
                continue

            x = 0
            y = i
            while y not in Stops:
                x += 1
                y -= 1
            x = x * 80 + 30
            y = y * 10 + 30

            for z, valz in enumerate(pieces):
                if vali == valz: 
                    self.screen.blit(images[z], (x, y))

        pygame.display.flip()

    def Run(self):
        while self.running:
            self.Events()
            self.Display()
            self.fps.tick(60)

pygame.init()

window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Chess.tom")

Play = Board(window, bg)
Play.Run()

pygame.quit()