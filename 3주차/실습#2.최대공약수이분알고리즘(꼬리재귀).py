def fastgcd1(m,n):
    def loop(m,n,k):
        if not (m == 0 or n == 0):
            if m % 2 == 0 and n % 2 == 0:
                return loop(m//2,n//2,2*k)
            elif m % 2 == 0 and n % 2 == 1:
                return loop(m//2,n,k)
            elif m % 2 == 1 and n % 2 == 0:
                return loop(m,n//2,k)
            elif m <= n:
                return loop(m,(n-m)//2,k)
            else:
                return loop(n,(m-n)//2,k)
        else:
            if m == 0:
                return abs(n*k)
            else: 
                return abs(m*k)
    return loop(m,n,1)
print(fastgcd1(48,18))
