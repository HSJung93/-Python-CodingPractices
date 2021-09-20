import sys, math, heapq

n, m= map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
distance = [math.inf] * (n+1)

for _ in range(m):
    fr, to, dist = map(int, sys.stdin.readline().split())
    graph[fr].append((to, dist))
    
# def get_smallest_node():
#     min_value = math.inf
#     index = 0
#     for i in range(1, n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     # distance of start node is 0
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]

#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
    
# dijkstra(start)

##
def dijkstar_heap(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        # check whether the node is visited 
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstar_heap(start)
##

for i in range(1, n+1):
    if distance[i] == math.inf:
        print("INF")
    else:
        print(distance[i])