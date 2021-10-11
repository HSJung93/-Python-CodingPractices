import sys, heapq
N = int(sys.stdin.readline())
l = []
for _ in range(N):
  heapq.heappush(l, int(sys.stdin.readline()))

for i in range(N):
  print(heapq.heappop(l))