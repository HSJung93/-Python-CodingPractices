import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
  arr.append( [x for x in sys.stdin.readline().rstrip()] )

visited = [[False] * N for _ in range(N)]

def dfs(i, j, val):
  visited[i][j] = True
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nx, ny = i + dx, j + dy
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == val:
      dfs(nx, ny, val)

cnt = 0

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      dfs(i, j, arr[i][j])
      cnt += 1

cnt2 = 0

for i in range(N):
  for j in range(N):
    if arr[i][j] == "R":
      arr[i][j] = "G"

visited = [[False] * N for _ in range(N)] 

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      dfs(i, j, arr[i][j])
      cnt2 += 1

print(cnt, cnt2)