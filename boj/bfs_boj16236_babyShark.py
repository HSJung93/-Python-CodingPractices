import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[0] * N for _ in range(N)]

for i in range(N):
  	graph[i] = list(map(int, sys.stdin.readline().split()))

moves = [
    (-1, 0),  # 위
    (0, -1),  # 왼쪽
    (1, 0),  # 아래
    (0, 1)  # 오른쪽
]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

weight, time, eat = 2, 0, 0


def isIn(nx, ny, N):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []  # 종료 조건을 위하여 큐를 하나 더 만드는 경우

    q.append([x, y])
    c = [[-1]*N for _ in range(N)]
    c[x][y] = time

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy

                if isIn(nx, ny, N) and c[nx][ny] == -1:
                    if graph[nx][ny] == 0 or graph[nx][ny] == weight:
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])

                    elif 0 < graph[nx][ny] < weight:
                        can_eat.append([nx, ny])

        # 종료 조건이 이동 후에 생기는 경우

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1

            graph[nx][ny] = 0
            return nx, ny, weight, c[x][y] + 1, eat


def search(weight, graph):
    for row in graph:
        for elm in row:
            if elm != 0 and elm < weight:
                return True
    return False


# while을 이용하여 bfs를 그때 그때 새롭게 돌린다. graph에 외부에 값을 저장해야 한다.
while search(weight, graph):
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)  # 그래프는 역시 변수에 없음

print(time)

"""
input:
3
0 0 1
0 0 0
0 9 0
output:
3

input:
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
output:
60
"""
