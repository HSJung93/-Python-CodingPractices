import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [ 0 for _ in range(n)]

for i in range(n):
  # 자신 이전의 작은 값들 중 최고의 dp값을 구한다
  for j in range(i):
    if a[i] > a[j] and dp[i] < dp[j]:
      dp[i] = dp[j]
  
  # 그 값에 1을 더하면 현재의 dp 값이다.

  dp[i] += 1

print(max(dp))