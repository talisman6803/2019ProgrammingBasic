### 6. 일반재귀 함수를 꼬리재귀 함수로 변환하기 
def adjust(ns):
    if len(ns) > 1:
        if ns[0] < ns[1]:
            return [ns[0]+1] + adjust(ns[1:])
        elif ns[0] > ns[1]:
            return [ns[0]-1] + adjust(ns[1:])
        else:
            return [ns[0]] + adjust(ns[1:])
    else:
        return ns

# print(adjust([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjust([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjust([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjust([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjust([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def adjustT(ns):
    def loop(ns,rs):
        if len(ns) > 1:
            if ns[0] < ns [1]:
                rs += [ns[0]+1]
                return loop(ns[1:],rs)
            elif ns[0] > ns[1]:
                rs += [ns[0]-1]
                return loop(ns[1:],rs)
            else:
                rs += [ns[0]]
                return loop(ns[1:],rs)
        else:
            return rs + ns
    return loop(ns,[])

### 7. 꼬리재귀 함수를 while 루프 함수로 변환하기

def adjustW(ns):
    rs = []
    while len(ns) > 1:
        if ns[0] < ns[1]:
            rs += [ns[0]+1]
        elif ns[0] > ns[1]:
            rs += [ns[0]-1]
        else:
            rs += [ns[0]]
        ns = ns[1:]
    return rs + ns

# print(adjustW([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjustW([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjustW([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustW([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustW([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

### 8. for 루프 함수로 만들기
def adjustF(ns):
    rs = []
    for i in range(len(ns)-1):
        if ns[i] < ns[i+1]:
            rs += [ns[i]+1]
        elif ns[i] > ns[i+1]:
            rs += [ns[i]-1]
        else:
            rs += [ns[i]]
    return rs

# print(adjustF([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjustF([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjustF([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustF([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustF([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
