def make_holes(board,no_of_holes):
    import random
    holeset=[]
    cnt = 0
    while (cnt != no_of_holes):
        i = random.randrange(0,4)
        j = random.randrange(0,4)
        if (board[i][j] != 0):
            board[i][j] = 0
            holeset.append((i,j))
            cnt += 1
    return (board, holeset)
