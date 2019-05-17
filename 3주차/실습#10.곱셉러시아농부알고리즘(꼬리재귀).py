def rsmult1(m,n):
    def loop(m,n,a):
        if n > 1:
            if n % 2 == 1:
                return loop(2*m,n//2,a+m)
            else:
                return loop(2*m,n//2,a)
        else:
            return m + a

    if n > 0:
        return loop(m,n,0)
    else:
        return 0
