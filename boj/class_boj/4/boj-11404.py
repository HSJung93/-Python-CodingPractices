import sys
import math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

dist = [[math.inf] * N for _ in range(N)]

for i in range(N):
  dist[i][i] = 0

for _ in range(M):
  fr, to, co = map(int, sys.stdin.readline().split())

  dist[fr-1][to-1] = min(co, dist[fr-1][to-1])

for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for d in dist:
  print(" ".join([str(x) if x != math.inf else "0" for x in d ]))