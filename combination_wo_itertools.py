rst = []

def combi_back(arr, visited, start, n, r):
  if r == 0:

    temp = []

    for i, num in enumerate(arr):
      if visited[i]:
        temp.append(num)

    rst.append(temp)

    return 

  for i in range(start, n):
    visited[i] = True
    combi_back(arr, visited, i+1, n, r-1)
    visited[i] = False

combi_back([1,2,3,4], [False]*4, 0, 3, 2)
print(rst)

rst = []

def combi_recur(arr, visited, depth, n, r):
  if r == 0:
    temp = []

    for i, num in enumerate(arr):
      if visited[i]:
        temp.append(num)

    rst.append(temp)

    return 

  if depth == n:
    print(r)
    print(visited)
    return

  visited[depth] = True
  combi_recur(arr, visited, depth+1, n, r-1)
  visited[depth] = False
  combi_recur(arr, visited, depth+1, n, r)

combi_recur([1,2,3,4], [False]*4, 0, 3, 2)
print(rst)