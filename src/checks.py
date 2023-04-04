def CheckIfCastles(pos, dest, board):
    pass


def CheckPawn(pos, dest, board):
    pass


def CheckKnight(pos, dest, board):
    posbs = []
    tries = [-17, -15, -10, -6, 6, 10, 15, 17]
    for i in tries:
        if -1 < pos + i < 63:
            posbs.append(pos + i)
    for y in posbs:
        if y == dest:
            return True
    return False


def CheckBishop(pos, dest, board):
    tries = [-9, -7, 7, 9]
    for x in range(4):
        for i in range(8):
            add = (i + 1) * tries[x]
            if 0 <= pos + add <= 63: break
            if pos + add == dest: return True
            if board[pos + add].islower() or board[pos + add].isupper(): break
    return False


def CheckRook(pos, dest, board):
    posbs = []
    walls1 = [0, 8, 16, 24, 32, 40, 48, 56]
    walls2 = [7, 15, 23, 31, 39, 47, 55, 64]
    direc = 1
    loc = pos + direc
    running = True
    while 0 <= loc <= 63:
        posbs.append(loc)
        if board[loc].islower() or board[loc].isupper():
            running = False
        loc += direc
        if loc in walls2:
            break
    
    direc = -1
    loc = pos + direc
    running = True
    while 0 <= loc <= 63:
        posbs.append(loc)
        if board[loc].islower() or board[loc].isupper():
            running = False
        loc += direc
        if loc in walls1:
            break
    
    tries = [-8, 8]
    posbs = []
    for i in tries:
        loc = pos + i
        while 0 <= loc <= 63:
            posbs.append(loc)
            if board[loc].islower() or board[loc].isupper():
                break
            loc += i
    for y in posbs:
        if y == dest:
            return True
    return False


def CheckQueen(pos, dest, board):
    pass


def CheckKing(pos, dest, board):
    pass


def CheckIfinCheck(pos, dest, board):
    pass
