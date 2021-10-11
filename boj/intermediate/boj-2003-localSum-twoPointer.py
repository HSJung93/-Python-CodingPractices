import sys
n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

lo = 0
hi = 1

tmp = arr[0]
cnt = 0

while lo < n:
  if tmp == m:
    cnt += 1
    
    # 일반적으로 앞에서 해결하지 말고 그때 해결해버리자
    tmp -= arr[lo]
    lo += 1
    
  if hi == n and tmp < m:
    break
  
  elif tmp < m:
    tmp += arr[hi]
    hi += 1
    
  elif tmp > m:
    tmp -= arr[lo]
    lo += 1
  
print(cnt)