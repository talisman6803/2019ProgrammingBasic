def insert(n,ss) :
    left = []
    cnt = 0
    while ss != [] :
        if n <= ss[0] :
            return [n] + ss
        else :
            cnt += 1
            left = ss[cnt]
            ss, left = ss[cnt:], left + ss[cnt:cnt]
    return left + ss
