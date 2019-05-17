def permutation1(n,k) :
    if k > 0 :
        return n * permutation1(n-1,k-1)
    else :
        return 1

def permutation2(n,k) :
    def loop(n,k,ans) :
        if k > 0 :
            return loop(n-1,k-1,ans*n)
        else :
            return ans
    return loop(n,k,1)
        
def permutation3(n,k) :
    ans = 1
    while k > 0 :
        ans = ans * n
        n -= 1
        k -= 1
    return ans
