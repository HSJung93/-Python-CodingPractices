import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

h = []

for _ in range(M):
  fr, to = map(int, sys.stdin.readline().split())
  graph[fr].append(to)
  indegree[to] += 1
  
for i in range(1, N+1):
  if indegree[i] == 0:
    heapq.heappush(h, i)
    
res = []
while h:
  now = heapq.heappop(h)
  res.append(now)
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      heapq.heappush(h, i)
      
print(*res)