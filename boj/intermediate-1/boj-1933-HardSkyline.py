import sys
from collections import deque
import heapq

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
  start, height, end = map(int, sys.stdin.readline().split())
  heapq.heappush(arr, (start, height))
  heapq.heappush(arr, (end, -height))

skyline = []
rst = []

x, h = heapq.heappop(arr)
rst.append(x)
rst.append(h)
# print(x, end = ' ')
# print(h, end = ' ')

while arr:

      
      
  