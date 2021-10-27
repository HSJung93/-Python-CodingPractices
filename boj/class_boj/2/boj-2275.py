import sys

T = int(sys.stdin.readline())


#  1  2  3  4  5
#0 1  2  3  4  5
#1 1  3  6  10 15
#2 

for _ in range(T):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())

  apt = [ i for i in range(1, n+1)] 

  for j in range(k):
    for i in range(1, n):
      apt[i] = apt[i] + apt[i-1]

  print(apt[n-1])



