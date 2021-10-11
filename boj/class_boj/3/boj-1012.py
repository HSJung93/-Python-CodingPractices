### ! 다음 조건 부분에서 이중리스트의 다음 좌표에서 실수가 잦다. 
### 재귀로 짤 때 함수 시작 부분에서 마킹

import sys

T = int(sys.stdin.readline())

def dfs(i, j, graph, visited):
  
  visited[i][j] = True
  graph[i][j] = 0
  
  for di, dj in [(0, -1),(0, 1),(-1, 0),(1, 0)]:
    ni, nj = i + di, j+dj
    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and graph[ni][nj] == 1:
      dfs(ni, nj, graph, visited)
  

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  graph = [[0] * M for _ in range(N)]
  for _ in range(K):
    m, n = map(int, sys.stdin.readline().split())
    graph[n][m] = 1
    
  cnt = 0
  
  visited = [[False]*M for _ in range(N)]
  
    
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        dfs(i, j, graph, visited)
        cnt += 1
        
  print(cnt)


"""
입력:
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

출력:
5
1

입력:
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

출력:
2

"""