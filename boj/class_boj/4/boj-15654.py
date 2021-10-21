import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for a in sorted(list(permutations(arr, M))):
  print(" ".join([str(x) for x in a]))