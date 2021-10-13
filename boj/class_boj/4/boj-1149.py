import sys
import math

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[math.inf,math.inf,math.inf] for _ in range(N+1)]
dp[1] = arr[0]
for i in range(2, N+1):
  dp[i][0] = arr[i-1][0]+ min(dp[i-1][1], dp[i-1][2])
  dp[i][1] = arr[i-1][1]+ min(dp[i-1][0], dp[i-1][2])
  dp[i][2] = arr[i-1][2]+ min(dp[i-1][0], dp[i-1][1])
print(min(dp[N][0], dp[N][1], dp[N][2]))