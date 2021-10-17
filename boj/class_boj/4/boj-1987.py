import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
  graph.append(list(sys.stdin.readline().strip()))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# def bfs():
  
#   q = set()
#   q.add((0, 0, graph[0][0]))

#   mx = 1

#   while q:
#     x, y, history= q.pop()

#     for dx, dy in moves:
#       nx, ny = x + dx, y + dy
#       # visited 조건이 아니라 history 조건으로
#       if 0 <= nx < R and 0 <= ny < C:
#         if graph[nx][ny] not in history:
#           mx = max(mx, len(history) + 1)
#           q.add((nx, ny, history + graph[nx][ny]))
          
#   return mx

# print(bfs())

ans = 0

def incode(char):
  return ord(char) - 65

def dfs(x, y, cnt):
  global ans
  ans = max(ans, cnt)

  for dx, dy in moves:
    nx, ny = x + dx, y + dy
    if 0 <= nx < R and 0 <= ny < C and visited[incode(graph[nx][ny])] == 0:
      visited[incode(graph[nx][ny])] = 1
      dfs(nx, ny, cnt+1)
      visited[incode(graph[nx][ny])] = 0

visited = [0] * 26
visited[incode(graph[0][0])]= 1
dfs(0, 0, 1)
print(ans)
