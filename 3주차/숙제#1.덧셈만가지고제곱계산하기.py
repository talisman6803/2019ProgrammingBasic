def square0(n) :
    def loop(n) :
        if n > 0 :
            return 2 * n - 1 + loop(n-1)
        else:
            return 0
    return loop(abs(n))

def square1(n) :
    def loop(n,ans) :
        if n > 0 :
            return loop(n-1,ans+2*n-1)
        else :
            return ans
    return loop(abs(n),0)

def square2(n) :
    n = abs(n)
    ans = 0
    while n > 0 :
        n -= 1
        ans += 2 * (n + 1) - 1
    return ans
