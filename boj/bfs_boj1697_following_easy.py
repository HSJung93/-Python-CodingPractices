## 거리를 이동하는데 bfs로 이동하여 최소의 거리를 찾는 문제

import sys, math
from collections import deque

MAX = 10**5

subin, brother = map(int, sys.stdin.readline().split())

q = deque()
q.append(subin)
dist = [math.inf] * (MAX + 1) 
dist[subin] = 0

while q:
    now = q.popleft()
    
    if now == brother:
        print(dist[now])
        break
    
    for next in (now-1, now+1, now*2):
        if 0 <= next <= MAX and dist[next] > dist[now] + 1:
            dist[next] = dist[now] + 1
            q.append(next)




