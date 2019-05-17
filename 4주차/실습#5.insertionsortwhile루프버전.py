def insertionsort(ns) :
    ss = []
    while ns != [] :
        ns, ss = ns[1:],insert(ns[0],ss)
    return ss
def insert(n,ss) :
    left = []
    while ss != [] :
        if n <= ss[0] :
            return left + [n] + ss
        else :
            ss, left = ss[1:], left + [ss[0]]
    return left + [n]
