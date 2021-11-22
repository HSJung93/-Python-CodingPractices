import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N, M = map(int, sys.stdin.readline().split())

  q = list(map(int, sys.stdin.readline().split()))

  mark = [0 for _ in range(N)]  
  mark[M] = 1
  cnt = 0

  while True:
    if q[0] == max(q):
      cnt += 1
      if mark[0] == 1:
        print(cnt)
        break
      else:
        del q[0]
        del mark[0]

    else:
      q.append(q[0])
      del q[0]
      mark.append(mark[0])
      del mark[0]