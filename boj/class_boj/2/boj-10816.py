import sys
from collections import defaultdict

N = int(sys.stdin.readline())

dd = defaultdict(int)

for num in list(map(int, sys.stdin.readline().split())):
  dd[num] += 1

M = int(sys.stdin.readline())
ans = []

for num in list(map(int, sys.stdin.readline().split())):
  ans.append(str(dd[num]))

print(" ".join(ans))
  