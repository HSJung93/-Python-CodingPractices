import sys
import heapq
import math

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
  fr, to, cost = map(int, sys.stdin.readline().split())
  graph[fr].append((cost, to))
  graph[to].append((cost, fr))

v1, v2 = map(int, sys.stdin.readline().split())

def dij(start, end):
  distance = [math.inf for _ in range(N+1)]
  h = [(0, start)]
  distance[start] = 0

  while h:
    cost_now, now = heapq.heappop(h)

    if distance[now] < cost_now:
      continue

    for cost_diff, nxt in graph[now]:
      cost_nxt = cost_now + cost_diff
      if cost_nxt < distance[nxt]:
        distance[nxt] = cost_nxt
        heapq.heappush(h, (cost_nxt, nxt))

  return distance[end]

# n1 -> n2 뿐 아니라 n2 -> n1 도 가능하다.
sm = min(dij(1, v1) + dij(v1, v2) + dij(v2, N), dij(1, v2) + dij(v2, v1) + dij(v1, N))

print(sm if sm != math.inf else -1)