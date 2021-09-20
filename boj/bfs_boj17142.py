# bfs시 맨 처음에 3개를 넣어버릴 수 있다.
# 아예 간편하게 길이를 위한 이중 리스트를 만들어 버리는게 편하다. 원래 것을 바꾸다 보면은 복잡해짐. 쉬운 문제만 그렇게 풀 수 있다.

from itertools import combinations
from collections import deque
import sys, math

input = sys.stdin.readline
         
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]        
n, m = map(int, input().split())

graph = []
starts = []
everySpace = 0

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 2: starts.append([i, j])
        if row[j] != 1: everySpace += 1

combi = list(combinations(starts, m))
result = math.inf

def isIn(nx, ny, n):
    return 0 <= nx < n and 0 <= ny < n

def bfs():
    # q에 넣는 것을 함수 밖에서 해도 된다. 
    # 함수의 인자가 없는게 편리?
    
    while q:
        x, y = q.popleft()
        
        # qsize로 구분할 필요 없음
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # visited == 0/ visited != 1/ visited == False/ dist == -1
            if isIn(nx, ny, n) and dist[nx][ny] == -1 and graph[nx][ny] != 1:
                q.append([nx, ny])
                dist[nx][ny] = dist[x][y] + 1

for i in combi:
    dist = [[-1] * n for i in range(n)]
    q = deque()
    
    for x, y in i:
        dist[x][y] = 0
        q.append([x, y])
        
    bfs()
    
    notVisited = 0
    for row in dist: notVisited += row.count(-1)
    
    if everySpace == (n * n - notVisited):
    
        max_n = 0
        for j in range(n):
            for k in range(n):
                if graph[j][k] != 1 and [j, k] not in starts:
                    max_n = max(max_n, dist[j][k])
                    
        result = min(result, max_n)

        
print(result if result != math.inf else -1)

"""
input:
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
output:
4

input:
7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
output:
-1
"""
