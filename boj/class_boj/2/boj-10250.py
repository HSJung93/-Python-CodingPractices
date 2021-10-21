import sys
T = int(sys.stdin.readline())
for _ in range(T):
  H, W, N = map(int, sys.stdin.readline().split())

  cnt = 0
  Done = False

  for room in range(1, W+1):
    for floor in range(1, H+1):
      cnt += 1
      if cnt == N:
        print(str(floor) + ("%02d" % room))
        Done = True
        break
    if Done:
      break


