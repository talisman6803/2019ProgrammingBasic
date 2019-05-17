def rsmult(m,n):
    ans = 0
    while n > 1 :
        if n % 2 == 1 :
            ans += m
            m = m * 2
            n = n // 2
        else :
            m = m * 2
            n = n // 2
    return m + ans
