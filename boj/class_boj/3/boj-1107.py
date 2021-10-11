import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

remote = {str(x) for x in range(10)}
if M > 0:
  remote -= set(map(str, sys.stdin.readline().split()))

cur = 100
min_cnt = abs(cur - N)

# 전 채널을 순회한다. 
for channel in range(1000000):
  for j in range(len(str(channel))):
    if str(channel)[j] not in remote:
      break
    elif len(str(channel)) - 1 == j:
      min_cnt = min(min_cnt, abs(channel - N) + len(str(channel)))
      
print(min_cnt)
    
    