# 카카오 2021 6번 문항과 유사
# import copy, sys

# N, M = map(int, sys.stdin.readline().split())

# matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# sm = copy.deepcopy(matrix)

# for i in range(N):
#   for j in range(N):
#     if i == 0 and j == 0:
#       pass
#     elif i == 0:
#       sm[0][j] += sm[0][j-1]
#     elif j == 0:
#       sm[i][0] += sm[i-1][0]
#     else:
#       sm[i][j] += sm[i-1][j] + sum(matrix[i][:j])

# for _ in range(M):
#   i, j, x, y = map(int, sys.stdin.readline().split())

#   if i == 1 and j == 1:
#     print(sm[x-1][y-1])
#   elif i == 1:
#     print(sm[x-1][y-1] - sm[x-1][j-2])
#   elif j == 1:
#     print(sm[x-1][y-1] - sm[i-2][y-1])
#   else:
#     print(sm[x-1][y-1] - sm[i-2][y-1] - sm[x-1][j-2] + sm[i-2][j-2])


import sys
n, m = map(int, sys.stdin.readline().split())
dp = [[0] * (n+1) for _ in range(n+1)]
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    dp[i+1][j+1] = (dp[i][j+1] + dp[i+1][j] - dp[i][j]) + s[i][j]

for i in range(m):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  print(dp[x2][y2] - (dp[x1 -1 ][y2] + dp[x2][y1-1] - dp[x1 - 1][y1 - 1]  ))