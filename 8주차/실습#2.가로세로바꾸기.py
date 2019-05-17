def transpose(board):
    transposed = []  
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        for i in range(len(row)):
            transposed[i].append(row[i])
    return transposed
