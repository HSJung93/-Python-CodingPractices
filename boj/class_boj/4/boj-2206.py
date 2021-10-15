import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, list(sys.stdin.readline().strip()))))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
  q = deque()
  # 시작 지점과 뚫을 수 있는 여부
  q.append((0, 0, 1))

  # 3차원 리스트로 벽을 뚫을 수 있는 상태 여부 기록. 
  # 인덱스 1의 값은 안 뚫고 갔을 때의 거리
  # 인덱스 0의 값은 뚫고 갔을 때의 거리
  visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]

  visited[0][0][1] = 1
  while q:
    x, y, w = q.popleft()

    if x == n-1 and y == m-1:
      return visited[x][y][w]

    for dx, dy in moves:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < m :
        # 벽을 뚫고 갈 수 있을 때
        if graph[nx][ny] == 1 and w == 1:
          visited[nx][ny][0] = visited[x][y][1] + 1
          q.append((nx, ny, 0))

        # 길을 가는데 방문 했는 지 안했는지에 따라서 둘 다 같은 로직
        elif graph[nx][ny] == 0 and visited[nx][ny][w] == -1:
          visited[nx][ny][w] = visited[x][y][w] + 1
          q.append((nx, ny, w))

  return -1


print(bfs())
