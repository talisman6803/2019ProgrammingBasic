def gcd(m,n):
    while n != 0 :
        tmp=m
        m=n
        n=tmp%n
    return abs(m)
