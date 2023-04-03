"""
To-dos: castle, check if he the piece can reach that square or not
"""
import pygame
from Pieces import *
from Checks import *

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = []
        self.Running = True
        self.WhiteToPlay = True
        self.bg = bg
        self.sprites = []
        self.fps = pygame.time.Clock()
        self.chose = False

    def events(self):
        #Ends the window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False

            #Checks if the mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 30 and pos[0] < 670 and pos[1] > 30 and pos[1] < 670:
                    Loc = int((pos[1] - 30) / 80) * 8 + int((pos[0] - 30) / 80)
                    if not self.chose:
                        self.Piece = self.board[Loc]
                        if self.Piece != "-":
                            if self.WhiteToPlay and not self.Piece.islower():
                                self.board[Loc] = "-"
                                self.chose = True
                                self.Loc = Loc
                                self.WhiteToPlay = False
                            elif not self.WhiteToPlay and self.Piece.islower():
                                self.board[Loc] = "-"
                                self.chose = True
                                self.Loc = Loc
                                self.WhiteToPlay = True
                    else:
                        if self.Loc != Loc:
                            if self.Piece == "p" or self.Piece == "P": self.works = CheckPawn(self.Loc, Loc)
                            elif self.Piece == "n" or self.Piece == "N": self.works = CheckKnight(self.Loc, Loc)
                            elif self.Piece == "b" or self.Piece == "B": self.works = CheckBishop(self.Loc, Loc)
                            elif self.Piece == "r" or self.Piece == "R": self.works = CheckRook(self.Loc, Loc)
                            elif self.Piece == "q" or self.Piece == "Q": self.works = CheckQueen(self.Loc, Loc)
                            elif self.Piece == "k" or self.Piece == "K": self.works = CheckKing(self.Loc, Loc)
                            if self.works:
                                if self.WhiteToPlay and not self.board[Loc].islower():
                                    self.board[Loc] = self.Piece
                                    self.chose = False
                                elif not self.WhiteToPlay and not self.board[Loc].isupper():
                                    self.board[Loc] = self.Piece
                                    self.chose = False

    def display(self):
        #Sets the background color as black and adds a background
        self.screen.fill("black")
        self.screen.blit(self.bg, (30, 30))

        #Turns the values inside the chess board into coordinates (To be redone)
        for i, val in enumerate(self.board):
            if i > 55:
                x = i - 56
                y = 590
            elif i > 47:
                x = i - 48
                y = 510
            elif i > 39:
                x = i - 40
                y = 430
            elif i > 31:
                x = i - 32
                y = 350
            elif i > 23:
                x = i - 24
                y = 270
            elif i > 15:
                x = i - 16
                y = 190
            elif i > 7:
                x = i - 8
                y = 110
            else:
                x = i
                y = 30
            x = x * 80 + 30

            #Places pieces on the according squares
            for x1, valx in enumerate(Pieces):
                if val == valx: self.screen.blit(Images[x1], (x, y))

        pygame.display.flip()

    def Run(self):
        self.board = InitBoard()
        print(self.board)
        while self.Running:
            self.events()
            self.display()
            self.fps.tick(60)

pygame.init()
window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Chess.Tom")
bg = pygame.image.load("./Python/Chess/V3/Images/Board.png")
bg = pygame.transform.scale(bg, (640, 640))
Play = Board(window)

Play.Run()

pygame.quit()