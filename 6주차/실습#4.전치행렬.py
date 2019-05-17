def transpose(mat):
    transposed = [list(x) for x in zip(*mat)]
    return transposed
