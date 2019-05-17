def insert(n,ss) :
    if ss != [] :
        if n <= ss[0] :
            return [n] + ss
        else :
            smallest = min(ss)
            ss.remove(smallest)
            return [smallest] + insert(n,ss)
    else :
        return n
