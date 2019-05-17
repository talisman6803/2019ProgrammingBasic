def insert(n,ss) :
    def loop(ss,left):
        if ss != [] :
            if n <= ss[0] :
                return [n] + ss
            else :
                left = [min(ss)]
                ss.remove(min(ss))
                return left + loop(ss,left)
        else :
            return n
    return loop(ss,[])
