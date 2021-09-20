import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
g = []

for _ in range(R):
  # list와 []는 다르다 list는 문자열을 쪼개 준다
  g.append(list(sys.stdin.readline().rstrip()))

for i in range(R):
  for j in range(C):
    if g[i][j] == "L":
      x, y = i, j
      
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def check(i, j, v):
  s = deque()
  s.append((i, j))
  v[i][j] = True
  
  while s:
    i, j = s.popleft()
    for dx, dy in moves:
      nx, ny = i + dx, j + dy
      if 0 <= nx < R and 0 <= ny < C and not v[nx][ny] and not g[nx][ny] == 'X':
        if g[nx][ny] == 'L':
          return True
        v[nx][ny] = True
        s.append((nx, ny))
      
  return False

def melt(i, j):
  q = deque()
  q.append((i, j))
  visited[i][j] = True
  while q:
    i, j = q.popleft()
    
    for dx, dy in moves:
      nx, ny = i + dx, j + dy
      
      if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
        if g[nx][ny] == 'X':
          g[nx][ny] = '.'
          visited[nx][ny] = True
        else:
          visited[nx][ny] = True
          q.append((nx, ny))
          
cnt = 0

while not check(x, y, [[False]*C for _ in range(R)]):

  cnt += 1
  visited = [[False]*C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      if g[i][j] != 'X' and not visited[i][j]:
        melt(i, j)
  
print(cnt)