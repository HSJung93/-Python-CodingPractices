import math, sys, itertools

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())

  point = []
  total_x = 0
  total_y = 0

  for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    point.append([x, y])
    total_x += x
    total_y += y

  ret = math.inf
  com = list(itertools.combinations(point, int(N/2)))
  com_len = int(len(com)/2)

  for elm in com[:com_len]:
    element = list(elm)

    x1_total = 0
    y1_total = 0

    for x1, y1 in element:
      x1_total += x1
      y1_total += y1

    x2_total = total_x - x1_total
    y2_total = total_y - y1_total

    ret = min(
      ret, math.sqrt(
        (x1_total - x2_total) ** 2 + 
        (y1_total - y2_total) ** 2
        ) 
      )

  print(ret)