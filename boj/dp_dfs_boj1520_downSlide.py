"""
dfs로 cnt하면 시간초과가 나온다. 아마도 visited를 갱신하는 연산에서?

dp로 풀어보자. 상하좌우의 결과값 중 이동할 수 있는 곳의 결과값을 더해주는 dp문제. 

input:
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

output:
3
"""

# from collections import deque
# import sys

# moves = [(+1, 0), (0, 1), (-1, 0), (0, -1)]
# # visited 불필요

# rowN, colN = map(int, sys.stdin.readline().split())

# graph = [[] for _ in range(rowN)]

# for i in range(rowN):
#     graph[i] = list(map(int, sys.stdin.readline().split()))
    
# def dfs(x, y, graph):
#     s = deque()
#     s.append((x, y))
#     visited = [[False] * colN for _ in range(rowN) ]
    
#     cnt = 0
    
#     while s:
#         x, y = s.pop()
#         visited[x][y] = True
        
#         if x == (rowN-1) and y == (colN-1):
#             cnt += 1

#             visited = [[False] * colN for _ in range(rowN) ]
            
#         for dx, dy in moves:
#             nx, ny = x + dx, y + dy
            
#             if 0 <= nx < rowN and 0 <= ny < colN and not visited[nx][ny] and graph[x][y] > graph[nx][ny]:
#                 s.append((nx, ny))
                
#     return cnt

# print(dfs(0, 0, graph))


###

import sys

moves = [(+1, 0), (0, 1), (-1, 0), (0, -1)]
# visited 불필요

rowN, colN = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(rowN)]

for i in range(rowN):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    
def dfs(dp, graph, rowN, colN, x, y):  
    
    print(x, y)
    for d in dp:
        print(d)
    
    if x == (rowN-1) and y == (colN-1):
        dp[x][y] = 1
        return
    
    if dp[x][y] != -1:
        return
    
    dp[x][y] = 0
        
    for dx, dy in moves:
        nx, ny = x + dx, y + dy    
        if 0 <= nx < rowN and 0 <= ny < colN  and graph[x][y] > graph[nx][ny]:
            dfs(dp, graph, rowN, colN, nx, ny)
            dp[x][y] += dp[nx][ny]
                

dp = [[-1] * colN for _ in range(rowN)]

dfs(dp, graph, rowN, colN, 0, 0)

print(dp)
    
    
    