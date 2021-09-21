from itertools import permutations
import math
import sys

N = int(sys.stdin.readline())
ineqs = list(sys.stdin.readline().split())
nums_min = range(N+1)
nums_max = range(9, 9-(N+1), -1)

combined_min = math.inf

for perm in permutations(nums_min, (N+1)):
  lmin = str(perm[0])
  BREAKED = False
  for i in range(N):
    if ineqs[i] == '>':
      if perm[i] > perm[i+1]:
        lmin += str(perm[i+1])
      else:
        BREAKED = True
        break
    else:
      if perm[i] < perm[i+1]:
        lmin += str(perm[i+1])
      else:
        BREAKED = True
        break
      
  if not BREAKED:
    combined_min = min(combined_min, int(lmin))
    
combined_max = -math.inf

for perm in permutations(nums_max, (N+1)):
  lmax = str(perm[0])
  BREAKED = False
  for i in range(N):
    if ineqs[i] == '>':
      if perm[i] > perm[i+1]:
        lmax += str(perm[i+1])
      else:
        BREAKED = True
        break
    else:
      if perm[i] < perm[i+1]:
        lmax += str(perm[i+1])
      else:
        BREAKED = True
        break
      
  if not BREAKED:
    combined_max = max(combined_max, int(lmax))
        
print(str(combined_max).zfill(N+1))
print(str(combined_min).zfill(N+1))
    
