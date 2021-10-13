import sys, heapq, math
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  fr, to, co = map(int, sys.stdin.readline().split())
  graph[fr].append((co, to))
  
start, end = map(int, sys.stdin.readline().split())

def dij(start):
  dist = [math.inf for _ in range(N+1)]
  h = [(0, start)]
  dist[start] = 0
  while h:
    cost_now, now = heapq.heappop(h)
    
    if dist[now] < cost_now:
      continue

    for cost_diff, nxt in graph[now]:
      cost_nxt = cost_now + cost_diff
      if dist[nxt] > cost_nxt:
        dist[nxt] = cost_nxt
        heapq.heappush(h, (cost_nxt, nxt))
   
  return dist[end]

print(dij(start))