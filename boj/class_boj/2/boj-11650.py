import sys
from operator import itemgetter

N = int(sys.stdin.readline())
arr  = []
for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=itemgetter(0, 1))

for x, y in arr:
  print(str(x) + " " + str(y))
