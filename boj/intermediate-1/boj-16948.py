import sys
from collections import deque

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

v = [[-1] * N for _ in range(N)]

q = deque()
q.append((r1, c1))
v[r1][c1] = 0

moves = [(-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1)]

while q:
  x, y = q.popleft()
  
  if x == r2 and y == c2:
    break
  
  for dx, dy in moves:
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == -1:
      v[nx][ny] = v[x][y] + 1
      q.append((nx, ny))
    
    
print(v[r2][c2])