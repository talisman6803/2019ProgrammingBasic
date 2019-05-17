def insertionsort(ns) :
    def loop(ns,ss) :
        if ns != [] :
            def insert(n,ss) :
                left = []
                while ss != [] :
                    if n <= ss[0] :
                        return left + [n] + ss
                    else :
                        ss, left = ss[1:], left + [ss[0]]
                return left + [n]
            return loop(ns[1:],insert(ns[0],ss))
        else :
            return ss
    return loop(ns,[])
