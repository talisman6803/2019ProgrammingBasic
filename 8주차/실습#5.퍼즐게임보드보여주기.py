def show_board(board):
    print()
    print('S','|','1','2','3','4')
    print('-','+','-','-','-','-')
    i = 1
    for row in board:
        print(i,'|', end=' ')
        for j in range(len(row)):
            if (j != 3): 
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

show_board([[0,3,0,0],[2,4,0,0],[3,1,2,0],[0,2,1,0]])
