N = int(input())
M = int(input())

graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))
  
plans = list(map(int, input().split()))

parents = [i for i in range(N+1)]

def find_parent(parents, node):
  if parents[node] != node:
    parents[node] = find_parent(parents, parents[node])
  return parents[node]

def union_parent(parents, i, j):
  parent_i = find_parent(parents, i)
  parent_j = find_parent(parents, j)
  
  if parent_i < parent_j:
    parents[parent_j] = parent_i
  else:
    parents[parent_i] = parent_j
    
for i in range(N):
  for j in range(i, N):
    if graph[i][j] == 1:
      union_parent(parents, i+1, j+1)

valid = True
  
for i in range(len(plans)-1):
  a, b = plans[i], plans[i+1]
  if find_parent(parents, a) != find_parent(parents, b):
    print("NO")
    valid = False
    break

if valid:
  print("YES")
