import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
truth = []
truthN, *truth = map(int, sys.stdin.readline().split())
truth = set(truth)

partys = []
possibles = []

for _ in range(M):
  members = []
  volume, *members = map(int, sys.stdin.readline().split())
  partys.append(set(members))
  possibles.append(1)
  
for _ in range(M):
  for i, party in enumerate(partys):
    if truth & party:
      possibles[i] = 0
      truth = truth | party
    
print(sum(possibles))