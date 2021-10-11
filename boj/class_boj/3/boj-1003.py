import sys
N = int(sys.stdin.readline())
for _ in range(N):
  M = int(sys.stdin.readline())
  if M == 0:
    print("1 0")
    continue
  if M == 1:
    print("0 1")
    continue
  dp = [[0, 0] for _ in range(M+1)]
  dp[0] = [1, 0]
  dp[1] = [0, 1]
  for i in range(2, M+1):
    dp[i][0], dp[i][1] = dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]
    
  print(" ".join([str(x) for x in dp[M]]))