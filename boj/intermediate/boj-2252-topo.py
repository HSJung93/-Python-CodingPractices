import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

g = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  g[a].append(b)
  indegree[b] += 1
  
def topo():
  result = []
  q = deque()
  for i in range(1, N+1):
    if indegree[i] == 0:
      q.append(i)
      
  while q:
    now = q.popleft()
    result.append(now)
    for i in g[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
        
  for i in result:
    print(i, end=' ')

topo()      