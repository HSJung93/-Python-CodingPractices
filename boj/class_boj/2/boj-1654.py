import sys
K, N = map(int, sys.stdin.readline().split())

lengths = []
for _ in range(K):
  lengths.append(int(sys.stdin.readline()))

def calc(lengths, mid):
  cnt = 0
  for l in lengths:
    cnt += l // mid
  
  return cnt

left = 1
right = max(lengths)

while left <= right:
  mid = (left + right) // 2

  if calc(lengths, mid) >= N:
    left = mid + 1
  else:
    right = mid -1 

print(right)
print(mid)
print(left)