import sys, heapq, math

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  fr, to, co = map(int, sys.stdin.readline().split())
  graph[fr].append((co, to))
  graph[to].append((co, fr))

def bfs(start):
  dist = [math.inf] * (n+1)
  h = [(0, start)]
  dist[start] = 0

  while h:
    dist_cur, cur = heapq.heappop(h)
    if dist[cur] < dist_cur:
      continue

    for dist_diff, nxt in graph[cur]:
      dist_nxt = dist_diff + dist_cur
      if dist[nxt] > dist_nxt:
        dist[nxt] = dist_nxt
        heapq.heappush(h, (dist_nxt, nxt))

  mx = -math.inf
  mx_node = 0
  for i in range(1, n+1):
    if dist[i] > mx and dist[i] != math.inf:
      mx = dist[i]
      mx_node = i

  return mx_node, mx

node, _ = bfs(1)
_, diameter = bfs(node)
print(diameter)
