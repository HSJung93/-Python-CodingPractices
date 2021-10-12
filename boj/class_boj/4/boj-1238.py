import sys
import heapq
import math

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  fr, to, co = map(int, sys.stdin.readline().split())
  graph[fr].append((co, to))

def dij(start, end):
  distance = [math.inf for _ in range(N+1)]
  distance[start] = 0
  h = []
  heapq.heappush(h, (0, start))
  while h:
    cost, now = heapq.heappop(h)

    if distance[now] < cost:
      continue

    for cost_nxt, nxt in graph[now]:
      if cost+cost_nxt < distance[nxt]:
        distance[nxt] = cost+cost_nxt
        heapq.heappush(h, (cost+cost_nxt, nxt))

  return distance[end]

mx = 0
for i in range(1, N+1):
  mx = max(mx, dij(i, X) + dij(X, i))

print(mx)





