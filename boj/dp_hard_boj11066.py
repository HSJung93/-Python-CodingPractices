import sys, math

t = int(sys.stdin.readline())

for _ in range(t):
    
    k = int(sys.stdin.readline())
    cost = list(map(int, sys.stdin.readline().split()))
    
    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]
    
    psum = [0] * (k+1)
    for i in range(1, k+1):
        psum[i] = psum[i-1] + cost[i-1]
    
    for d in range(1, k):
        for tx in range(1, k-d+1):
            ty = tx + d
            dp[tx][ty] = math.inf
            
            for mid in range(tx, ty):
                dp[tx][ty] = min(dp[tx][ty], dp[tx][mid] + dp[mid+1][ty] + psum[ty] - psum[tx-1])
                
    print(dp[1][k])