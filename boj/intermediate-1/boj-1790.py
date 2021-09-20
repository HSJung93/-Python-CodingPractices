import sys
N, k = map(int, sys.stdin.readline().split())

def calc(N):
  ans = 0
  # 543
  # 543 - 100 + 1
  size = len(str(N)) # 3
  ans = 0
  for s in range(size, 0, -1):
    ans += (N - 10**(s-1) + 1) * s 
    N = 10**(s-1)-1
      
  return ans

calc_N = calc(N)

if calc_N < k:
  print(-1)
else:
  l = 1
  r = calc_N
  ans = 0
  while l <= r:
    mid = (l+r)// 2
    length = calc(mid)
    if k > length:
      l = mid + 1
    else:
      ans = mid
      r = mid - 1
      
  s = str(ans)
  l = calc(ans)
  
  print(s[len(s)-(l-k)-1])