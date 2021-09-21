import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

visited = [False] * 101
mp = {}
time = [0] * 101

for _ in range(N+M):
    fr, to = map(int, sys.stdin.readline().split())
    mp[fr] = to

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()

        for i in range(1, 7):
            next = now + i
            if 0 < next <= 100 and not visited[next]:
                if next in list(mp.keys()):
                    next = mp[next]

                if not visited[next]:

                    q.append(next)
                    visited[next] = True
                    time[next] = time[now] + 1


bfs(1)

print(time[100])

