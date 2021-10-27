from operator import itemgetter
import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
  x, y = map(int, sys.stdin.readline().split())
  arr.append([x, y])

arr.sort(key=itemgetter(1, 0))

for x, y in arr:
  print(str(x) + " " + str(y))