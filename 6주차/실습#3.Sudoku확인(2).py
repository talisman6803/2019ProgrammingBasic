def issudoku(mat):
    listt = []
    for i in range(len(mat)):
        listt += mat[i]
    listt.sort()
    for i in range(len(mat)**2):
        if listt[i] != i + 1:
            return False
    return True
