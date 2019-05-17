def issudoku(mat):
    chk = [0] * (len(mat)**2)
    for i in range(len(mat)):
        for j in range(len(mat)):
            if chk[mat[i][j]-1] == 0:
                chk[mat[i][j]-1] = 1
            else:
                return False
    return True
