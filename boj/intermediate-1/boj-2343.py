import sys
N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

l = max(times)
r = sum(times)

def blueraySize(m):
  blueray = 0
  cnt = 1
  for time in times:
    # blueray += time
    # if blueray > m:
    #   blueray = time
    #   cnt += 1
    #   if cnt > M:
    #     return False
    
    if blueray + time > m:
      cnt += 1
      blueray = 0
    blueray += time
    
    if cnt > M:
      return False

  return True
    
ans = r

while l <= r:
  
  m = (l+r)//2
  
  if blueraySize(m):
    r = m-1
    ans = min(ans, m)
  else:
    l = m+1
    
print(ans)
