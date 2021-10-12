import sys
N, M = map(int, sys.stdin.readline().split())

sn = set()
sm = set()

for _ in range(N):
  sn.add(sys.stdin.readline().rstrip())

for _ in range(M):
  sm.add(sys.stdin.readline().rstrip())

s = sn&sm
print(len(s))
a = list(s)
a.sort()
for word in a:
  print(word)
