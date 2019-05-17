def insertionsort(ns) :
    def loop(ns,ss) :
        if ns != []:
            num1=ns[0]
            ns.remove(num1)
            ss=num1
            return loop(ns,ss)
        else :
            return ss
    return loop(ns,[])
