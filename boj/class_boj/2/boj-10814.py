import sys
N = int(sys.stdin.readline())

arr = []

for _ in range(N):
  arr.append(list( sys.stdin.readline().split()))

arr.sort(key= lambda x:int(x[0]))

for a in arr:
  print(" ".join(a))