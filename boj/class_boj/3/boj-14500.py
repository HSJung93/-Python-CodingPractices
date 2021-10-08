import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + mx * (3 - idx):
        return

    if idx == 3:
        ans = max(ans, total)
        return
        
    for i in range(4):
        nr, nc = r + moves[i][0], c + moves[i][1]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
            if idx == 1:
                visited[nr][nc] = 1
                dfs(r, c, idx + 1, total + arr[nr][nc])
                visited[nr][nc] = -1
            visited[nr][nc] = 1
            dfs(nr, nc, idx + 1, total + arr[nr][nc])
            visited[nr][nc] = -1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [([-1] * M) for _ in range(N)]
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
mx = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visited[r][c] = -1

print(ans)

"""
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

19

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

20

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1

7
"""