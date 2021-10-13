import sys
from collections import deque

V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

for _ in range(V):
  c = list(map(int, sys.stdin.readline().split()))
  for e in range(1, len(c)-2, 2):
    graph[c[0]].append((c[e+1], c[e]))

def bfs(start):
  dist = [-1] * (V+1)
  q = deque()
  q.append(start)
  dist[start] = 0
  mx = [0, start]

  while q:
    now = q.popleft()
    for cost_diff, nxt in graph[now]:
      if dist[nxt] == -1:
        dist[nxt] = dist[now] + cost_diff
        q.append(nxt)
        if mx[0] < dist[nxt]:
          mx = dist[nxt], nxt

  # 가장 먼 거리, 가장 먼 거리의 노드
  return mx

# 임의 노드에서 가장 거리가 먼 노드
# 로부터 가장 먼 거리가 트리의 지름이다.
print(bfs(bfs(1)[1])[0])
        
