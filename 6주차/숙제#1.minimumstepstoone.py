def minsteps(n):
    memo = [0] * (n + 1)
    for i in range(n+1):
        if i == 0 or i == 1:
            continue
        elif i > 1:
            memo[i] = 1 + memo[i-1]
            if i % 2 == 0:
                memo[i] = min(memo[i], 1 + memo[i//2])
            if i % 3 == 0:
                memo[i] = min(memo[i], 1 + memo[i//3])
    return memo[n]
