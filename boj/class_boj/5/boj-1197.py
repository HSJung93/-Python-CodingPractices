import sys

V, E = map(int, sys.stdin.readline().split())

edges = []

for _ in range(E):
  edges.append(list(map(int, sys.stdin.readline().split())))

edges.sort(key = lambda x:x[2])

parents = [i for i in range(V+1)]

def find(parents, x):
  if parents[x] != x:
    parents[x] = find(parents, parents[x])
  return parents[x]

def union(a, b):
  a = parents[a]
  b = parents[b]

  if a < b:
    parents[b] = a
  else:
    parents[a] = b

weight = 0

for a, b, w in edges:
  if find(parents, a) != find(parents, b):
    union(a, b)
    weight += w

print(weight)