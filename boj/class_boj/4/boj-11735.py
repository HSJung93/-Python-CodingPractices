import sys

sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

parents = [0 for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(start, graph, parents):
  for i in graph[start]:
    if parents[i] == 0:
      parents[i] = start
      dfs(i, graph, parents)
      
dfs(1, graph, parents)

for i in range(2, N+1):
  print(parents[i])