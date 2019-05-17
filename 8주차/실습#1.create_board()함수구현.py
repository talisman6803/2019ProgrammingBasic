import random
def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)
    n1 = seed[0]
    n2 = seed[1]
    n3 = seed[2]
    n4 = seed[3]
    list = [[n1,n2,n3,n4], [n3,n4,n1,n2], [n2,n1,n4,n3], [n4,n3,n2,n1]]
    return list
print(create_board())
