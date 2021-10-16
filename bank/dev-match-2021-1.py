import copy
from collections import deque

def drop(where, color, graph):
    
    new = copy.deepcopy(graph)
    
    index = where - 1
    for i in range(SIX):
        if new[i][index] == 0:
            depth = i
    
    new[depth][index] = color
    
    return new

def howmany(i, j, x, graph):
    new = copy.deepcopy(graph)
    visited = [[0] * SIX for _ in range(SIX)]
    q = deque()
    visited[i][j] = 1
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIX and 0 <= ny < SIX and not visited[nx][ny] and new[nx][ny] == new[i][j]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                
                
    return sum(map(sum, visited))
        

def findPop(graph):
    for i in range(SIX):
        for j in range(SIX):
            if graph[i][j] != 0:
                cnt = 0 
                cnt = howmany(i, j, graph[i][j], graph)
                if cnt >= 3:
                    return [i, j]
            
    return [-1, -1]

moves = [(-1, 0),(1, 0),(0, -1),(0, 1)]
SIX = 6

def doPop(graph, a, b):
    new = copy.deepcopy(graph)
    
    visited = [[0] * SIX for _ in range(SIX)]
    
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIX and 0 <= ny < SIX and not visited[nx][ny] and new[nx][ny] == new[a][b]:
                new[nx][ny] = 0
                q.append((nx, ny))
                
    new[a][b] = 0
              
    # print("new!")  
    # for n in new:
    #   print(n)
    # print()
                
    for i in range(SIX):
        temp = []
        for j in range(SIX-1, -1, -1):
            if new[j][i] != 0:
                temp.append(new[j][i])
                
        for j in range(SIX-1, -1, -1):
            if temp:
                new[j][i] = temp[0]
                temp = temp[1:]
            else:
                new[j][i] = 0
                
    return new
            

def solution(macaron):
    answer = []

    graph = [[0]*SIX for _ in range(SIX)]
    
    for where, color in macaron:
        graph = drop(where, color, graph)
        
        while findPop(graph) != [-1, -1]:
            x, y = findPop(graph)
            graph = doPop(graph, x, y)
            # for g in graph:
            #   print(g)
            # print()
            
    for i in range(SIX):
        
        temp = ""
        
        for j in range(SIX):
            temp += str(graph[i][j])
            
        answer.append(temp)
    
    return answer
  
print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]))


for x in range(3,4):
  print(x)