import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))
  
young = 0
old = []

for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      young += 1
    elif graph[i][j] == 1:
      old.append([i, j])

def bfs():
  
  # dist를 visited 겸용으로 사용한다.
  dist = [[-1] * M for _ in range(N)]
  q = deque()
  
  # 여러 스타트 지점을 두어 bfs로 길이를 계산 하도록 한다.
  for start in old:
    q.append( [0] + start )
    i, j = start
    dist[i][j] = 0
    
  max_ = 0
  # 총 이동한 지점들 갯수 계산
  count = 0
    
  while q:
    # q 길이에 관한 코드는 거리 혹은 시간이 한 칸 이동 이외의 변수로도 증감할 때 필요하다. 
    # 즉 이 문제에서는 필요가 없음
    # for _ in range(len(q)):
    
    d, x, y = q.popleft()
    
    # 길이에 1 더하는 기준은 한 칸 이동하느냐
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1 and graph[nx][ny] == 0:
        dist[nx][ny] = d+1
        max_ = max(max_, d+1)
        count += 1
        q.append((d+1, nx, ny))
  
  if young == count:
    print(max_)
  elif young > count:
    print(-1)
    
bfs()
      