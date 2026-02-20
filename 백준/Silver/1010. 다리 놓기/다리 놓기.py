T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    
    for n in range(M + 1):
        for k in range(min(n, N) + 1):
            if k == 0 or k == n:
                dp[n][k] = 1
            else:
                dp[n][k] = dp[n-1][k-1] + dp[n-1][k]
    
    print(dp[M][N])