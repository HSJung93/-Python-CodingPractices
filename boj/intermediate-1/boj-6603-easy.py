import sys
from itertools import combinations

while True:
  text = sys.stdin.readline().split()
  if text[0] == '0':
    break
  N, *S = text
  for comb in list(combinations(S, 6)):
    print(' '.join(list(comb)))
    
  print()