import sys, math

T = int(sys.stdin.readline())

def bellman_ford():
  global isPossible

  for i in range(1, N+1):
    for now in range(1, N+1):
      for dist_diff, nxt in graph[now]:
        dist_nxt = dist_diff + dist[now]
        if dist[now] != math.inf and dist[nxt] > dist_nxt:
          dist[nxt] = dist_nxt
          if i == N:
            isPossible = False

for _ in range(T):
  N, M, W = map(int, sys.stdin.readline().split())
  dist = [math.inf for _ in range(N+1)]

  graph = [[] for _ in range(N+1)]

  for _ in range(M):
    S, E, T = map(int, sys.stdin.readline().split())
    graph[S].append((T, E))
    graph[E].append((T, S))

  for _ in range(W):
    S, E, T = map(int, sys.stdin.readline().split())
    graph[S].append((-T, E))

  isPossible = True

  bellman_ford()

  print("NO" if isPossible else "YES")
