import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

g = [[] for _ in range(N+1)]
bg = [[] for _ in range(N+1)]
ind = [0] * (N+1)
rst = [0] * (N+1)
chk = [0] * (N+1)

q = deque()

for _ in range(M):
  a, b, c = map(int, sys.stdin.readline().split())
  g[a].append((b, c))
  bg[b].append((a, c))
  ind[b] += 1
  
start, end = map(int, sys.stdin.readline().split())

q.append(start)

def topo():
  while q:
    cur = q.popleft()
    for next, cost in g[cur]:
      ind[next] -= 1
      rst[next] = max(rst[next], rst[cur]+cost)
      if ind[next] == 0:
        q.append(next)
        
  cnt = 0
  q.append(end)
  while q:
    cur = q.popleft()
    for prev, cost in bg[cur]:
      if rst[cur] - rst[prev] == cost:
        cnt += 1
        if chk[prev] == 0:
          q.append(prev)
          chk[prev] = 1
          
  print(rst[end])
  print(cnt)

topo()

"""
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7

12
5
"""