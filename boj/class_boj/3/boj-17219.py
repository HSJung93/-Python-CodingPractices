import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

dic = defaultdict(str)

for _ in range(N):
  ID, PASSWORD = sys.stdin.readline().rstrip().split(" ")
  dic[ID] = PASSWORD

for _ in range(M):
  print(dic[sys.stdin.readline().rstrip()])

