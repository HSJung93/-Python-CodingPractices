import sys
from operator import itemgetter
N = int(sys.stdin.readline())

time = []

for _ in range(N):
  fr, to = map(int, sys.stdin.readline().split())
  time.append((fr, to))

time.sort(key=itemgetter(1, 0))

cnt = 1
end = time[0][1]

for i in range(1, N):
  if time[i][0] >= end:
    cnt += 1
    end = time[i][1]

print(cnt)
