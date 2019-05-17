def isidentity(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(size):
            if i == j and sqmat[i][j] != 1 :
                return False
            elif i != j and sqmat[i][j] != 0 :
                return False
    return True
