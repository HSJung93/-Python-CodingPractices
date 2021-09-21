import sys
N = int(sys.stdin.readline())

g = [[] for _ in range(N+1)]

for _ in range(N-1):
  fr, to = map(int, sys.stdin.readline().split())
  g[fr].append(to)
  g[to].append(fr)
  
M = int(sys.stdin.readline())

parent = [i for i in range(N+1)]
d = [0] * (N+1)
v = [0] * (N+1)

def dfs(x, depth):
  v[x] = True
  d[x] = depth
  for next in g[x]:
    if v[next]:
      continue
    parent[next] = x
    dfs(next, depth+1)
    
dfs(1, 0)

def lca(a, b):
  while d[a] != d[b]:
    if d[a] > d[b]:
      a = parent[a]
    else:
      b = parent[b]
  
  while a != b:
    a = parent[a]
    b = parent[b]
    
  return a

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  print(lca(a, b))