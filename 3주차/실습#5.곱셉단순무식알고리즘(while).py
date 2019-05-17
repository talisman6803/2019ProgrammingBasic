def mult(m,n):
    ans = 0
    while n>0 :
        ans += m
        n -= 1
    return ans
print(mult(3,6))
