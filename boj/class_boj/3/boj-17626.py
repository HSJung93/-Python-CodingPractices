import sys
import math

N = int(sys.stdin.readline())

dp = [0] * (N+1)
dp[1] = 1

for i in range(2, n+1):
    if i == int(math.sqrt(i)) ** 2:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n+1):
    for j in range(1, int(math.sqrt(i))+1):
        dp[i] = min(dp[i], dp[j*j] + dp[i-j*j])

print(dp[n])
