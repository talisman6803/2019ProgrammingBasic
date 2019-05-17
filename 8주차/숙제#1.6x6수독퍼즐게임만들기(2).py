import random
def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    n1 = seed[0]
    n2 = seed[1]
    n3 = seed[2]
    n4 = seed[3]
    n5 = seed[4]
    n6 = seed[5]
    list = [[n1,n2,n3,n4,n5,n6], [n4,n5,n6,n1,n2,n3], [n3,n1,n2,n6,n4,n5], [n6,n4,n5,n3,n1,n2], [n2,n3,n1,n5,n6,n4], [n5,n6,n4,n2,n3,n1]]
    return (list)
def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if (level == "상"):
        return 18
    elif (level == "중"):
        return 15
    else:
        return 12
def make_holes(board,no_of_holes):
    import random
    temp = [[],[],[],[],[],[]]
    for i in range(6):
        for j in range(6):
            temp[i].append(board[i][j])
    count = 0
    while (count != no_of_holes):
        i = random.randrange(0,6)
        j = random.randrange(0,6)
        if (temp[i][j] != 0):
            temp[i][j] = 0
            count += 1
    return temp
def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        print(i,'|', end=' ')
        for j in range(len(row)):
            if (j != 5): 
                if (row[j]==0):
                    print('.', end=' ')
                else:
                    print(row[j], end=' ')
            else:
                if (row[j]==0):
                    print('.')
                else:
                    print(row[j])
        i += 1
def transpose(board):
    transposed = []  
    for _ in range(len(board)):
        transposed.append([])
    for row in board:
        for i in range(len(row)):
            transposed[i].append(row[i])
    return transposed
def shuffle_ribbons1(board) :
    top_onethird = board[:2]
    random.shuffle(top_onethird)
    mid_twothird = board[2:4]
    random.shuffle(mid_twothird)
    bottom_threethird = board[4:]
    random.shuffle(bottom_threethird)
    return top_onethird + mid_twothird + bottom_threethird
def shuffle_ribbons2(board) :
    top_half = board[:3]
    random.shuffle(top_half)
    bottom_half = board[3:]
    random.shuffle(bottom_half)
    return top_half + bottom_half
def get_integer(message,i,j):
    number = input(message)
    while not (i<=int(number)<=j):
        number = input(message)
    return int(number)
def create_solution_board(board):
    board = shuffle_ribbons1(board)
    board = transpose(board)
    board = shuffle_ribbons2(board)
    board = transpose(board)
    return board
def sudok6x6():
    b0=create_board()
    b0=create_solution_board(b0)
    level=get_level()
    b1=make_holes(b0,level)
    show_board(b1)
    cnt = 0
    while cnt != level:
        j = get_integer("가로줄번호(1~6): ",1,6) - 1
        i = get_integer("세로줄번호(1~6): ",1,6) - 1
        if b1[i][j] != 0:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~6): ",1,6)
        if n == b0[i][j]:
            b1[i][j] = n
            show_board(b1)
            cnt += 1
        else:
            print(n,"이(가) 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")
