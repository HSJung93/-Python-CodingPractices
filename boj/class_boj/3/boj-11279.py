import sys
import heapq

N = int(sys.stdin.readline())
h = []

for _ in range(N):
  number = int(sys.stdin.readline())
  if number == 0:
    if not h:
      print(0)
    else:
      print(-heapq.heappop(h))
  else:
    heapq.heappush(h, -number)

