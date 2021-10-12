import sys
N, M = map(int, sys.stdin.readline().split())
import math

dist = [[math.inf] * N for _ in range(N)]
for i in range(N):
  dist[i][i] = 0

for _ in range(M):
  fr, to = map(int, sys.stdin.readline().split())
  i, j = fr - 1, to - 1
  dist[i][j] = 1
  dist[j][i] = 1

for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

min_val = math.inf
result = -1
for i, val in enumerate(list(map(sum, dist))):
  if val < min_val:
    result = i
    min_val = val

print(result+1)

