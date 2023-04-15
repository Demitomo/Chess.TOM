def InCheck():
    pass


def CheckPawn(pos, board):
    if board[pos].islower(): white = False
    else: white = True
    
    posbs = []
    stops = [0, 8, 16, 24, 32, 40, 48, 56]
    x = 0
    y = 0
    while pos not in stops:
        pos -= 1
        x += 1
    y = int(pos / 8)

    if white: tries = [[0, -1], [0, -2], [-1, -1], [1, -1]]
    else: tries = [[0, 1], [0, 2], [-1, 1], [1, 1]]

    x1 = x + tries[0][0]
    y1 = y + tries[0][1]
    if board[y1 * 8 + x1] == "-": posbs.append(y1 * 8 + x1)

    x1 = x + tries[1][0]
    y1 = y + tries[1][1]
    if white:
        if board[y1 * 8 + x1] == "-" and y == 6: posbs.append(y1 * 8 + x1)
    else:
        if board[y1 * 8 + x1] == "-" and y == 1: posbs.append(y1 * 8 + x1)
    
    x1 = x + tries[2][0]
    y1 = y + tries[2][1]
    if white:
        if board[y1 * 8 + x1].islower(): posbs.append(y1 * 8 + x1)
    else:
        if board[y1 * 8 + x1].isupper(): posbs.append(y1 * 8 + x1)
    
    x1 = x + tries[3][0]
    y1 = y + tries[3][1]
    if white:
        if board[y1 * 8 + x1].islower(): posbs.append(y1 * 8 + x1)
    else:
        if board[y1 * 8 + x1].isupper(): posbs.append(y1 * 8 + x1)
    
    return posbs


def CheckKnight(pos, board):
    posbs = []
    stops = [0, 8, 16, 24, 32, 40, 48, 56]
    x = 0
    y = 0
    while pos not in stops:
        pos -= 1
        x += 1
    y = int(pos / 8)

    tries = [[-1, -2], [-2, -1], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]
    for i in tries:
        x1 = x + i[0]
        y1 = y + i[1]
        dest = y1 * 8 + x1

        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if board[pos].islower() and board[dest].islower(): continue
            elif board[pos].isupper() and board[dest].isupper(): continue
            posbs.append(dest)

    return posbs

def CheckBishop(pos, board):
    if board[pos].islower(): white = False
    else: white = True

    posbs = []
    stops = [0, 8, 16, 24, 32, 40, 48, 56]
    x = 0
    y = 0
    while pos not in stops:
        pos -= 1
        x += 1
    y = int(pos / 8)

    tries = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for i in tries:
        x1 = x + i[0]
        y1 = y + i[1]
        dest = y1 * 8 + x1

        while 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if white and board[dest].isupper(): break
            elif not white and board[dest].islower(): break
            posbs.append(dest)
            if board[dest].isupper() or board[dest].islower(): break
            x1 += i[0]
            y1 += i[1]
            dest = y1 * 8 + x1
    
    return posbs


def CheckRook(pos, board):
    if board[pos].islower(): white = False
    else: white = True

    posbs = []
    stops = [0, 8, 16, 24, 32, 40, 48, 56]
    x = 0
    y = 0
    while pos not in stops:
        pos -= 1
        x += 1
    y = int(pos / 8)

    tries = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in tries:
        x1 = x + i[0]
        y1 = y + i[1]
        dest = y1 * 8 + x1

        while 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if white and board[dest].isupper(): break
            elif not white and board[dest].islower(): break
            posbs.append(dest)
            if board[dest].isupper() or board[dest].islower(): break
            x1 += i[0]
            y1 += i[1]
            dest = y1 * 8 + x1
    
    return posbs


def CheckQueen(pos, board):
    if board[pos].islower(): white = False
    else: white = True

    posbs = []
    stops = [0, 8, 16, 24, 32, 40, 48, 56]
    x = 0
    y = 0
    while pos not in stops:
        pos -= 1
        x += 1
    y = int(pos / 8)

    tries = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    for i in tries:
        x1 = x + i[0]
        y1 = y + i[1]
        dest = y1 * 8 + x1

        while 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if white and board[dest].isupper(): break
            elif not white and board[dest].islower(): break
            posbs.append(dest)
            if board[dest].isupper() or board[dest].islower(): break
            x1 += i[0]
            y1 += i[1]
            dest = y1 * 8 + x1
    
    return posbs


def CheckKing(pos, board):
    if board[pos].islower(): white = False
    else: white = True

    posbs = []
    stops = [0, 8, 16, 24, 32, 40, 48, 56]
    x = 0
    y = 0
    while pos not in stops:
        pos -= 1
        x += 1
    y = int(pos / 8)

    tries = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    for i in tries:
        x1 = x + i[0]
        y1 = y + i[1]
        dest = y1 * 8 + x1
        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
            if white and board[dest].isupper(): continue
            elif not white and board[dest].islower(): continue
            posbs.append(dest)
    
    return posbs