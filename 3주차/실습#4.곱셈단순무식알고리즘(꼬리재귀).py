def mult2(m,n) :
    def loop(n,ans) :
        if n > 1 :
            return loop(n-1, ans+m)
        else :
            return ans
    return loop(n,m)
