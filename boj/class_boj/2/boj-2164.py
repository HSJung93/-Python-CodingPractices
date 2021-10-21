import sys

N = int(sys.stdin.readline())

square = 2

while True:
  if N == 1 or N == 2:
    print(N)
    break
  square *= 2
  if (square >= N):
    print((N - (square//2))*2)
    break