# 크루스칼 알고리즘으로 푸는 방법

def solution(n, costs):
    parent = [i for i in range(n+1)]
    
    edges= []
    
    for fr, to, cost in costs:
        edges.append((cost, fr, to)) 
        
    edges.sort()
    
    answer = 0
    
    for cost, fr, to in edges:
        if find_parent(parent, fr) != find_parent(parent, to):
            union_parent(parent, fr, to)
            answer += cost
    
    return answer

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b
        
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

# dijkstart_heap으로 푸는 방법

import heapq

def solution(n, costs):
    answer = 0
    
    g = [[] for _ in range(n)]
    visited = [False] * n
    priority = []
    
    for a, b, cost in costs:
        g[a].append((b, cost))
        g[b].append((a, cost))
        
    heapq.heappush(priority, (0, 0))
    
    while False in visited:
        now_cost, now = heapq.heappop(priority)
        if visited[now]:
            continue
        
        visited[now] = True
        answer += now_cost
        
        for next, next_cost in g[now]:
            if visited[next]:
                continue
            else:
                heapq.heappush(priority, (next_cost, next))
                          
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))