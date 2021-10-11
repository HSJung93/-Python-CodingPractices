import sys
N = int(sys.stdin.readline())
t = [0]
p = [0]
for _ in range(N):
  ti, pi = map(int, sys.stdin.readline().split())
  t.append(ti)
  p.append(pi)
  
dp = [0] * (N+1) + [0]

for i in range(N, 0, -1):
  if i == N and t[i] == 1:
    dp[i] = p[i]
    continue
  if i+1 <= N:
    dp[i] = max(dp[i], dp[i+1])
    if i+t[i]-1 <= N:
      dp[i] = max(dp[i], p[i]+dp[i+t[i]])
      
print(dp[1])
  
  
# dp[n] = max(dp[n+1], p[n]+dp[n+t[n]]) 

#          1 2 3 4 5 6 7
#                  15 0 0