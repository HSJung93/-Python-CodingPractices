import sys
from collections import deque

N = int(sys.stdin.readline())
s = deque()
h = deque()
e = deque()
for _ in range(N):
  start, height, end = map(int, sys.stdin.readline().split())
  s.append(start)
  h.append(height)
  e.append(end)

res = []
s_start = s.popleft()
h_prev = h.popleft()
res.append(s_start)
res.append(h_prev)
for i in range(1, N):
  s_next = s.popleft()
  h_next = h.popleft()
  end = e.popleft()
  print(res)
  
  if s_next > end:
    print("too par")
    res.append(end)
    res.append(0)
    res.append(s_next)
    res.append(h_next)
    h_prev = h_next
    continue
  if h_prev < h_next:
    print("higher")
    res.append(s_next)
    res.append(h_next)
    h_prev = h_next
    continue
  
print(res)