def fastmult(m,n) :
    ans = 0
    while n > 0 :
        if n % 2 == 0:
            m = m * 2
            n = n // 2
        else :
            n -= 1
            ans += m
    return ans
