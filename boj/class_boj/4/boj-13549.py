import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
mx = 100000
time = [mx] * (mx + 1)

q = deque()
q.append((N, 0))
time[N] = 0

while q:
  now, time_now = q.popleft()
  for nxt in [2 * now]:
    if 0 <= nxt <= mx and time[nxt] > time_now:
      time[nxt] = time_now
      q.append((nxt, time_now))
  for nxt in [now+1, now-1]:
    if 0 <= nxt <=mx and time[nxt] > time_now + 1:
      time[nxt] = time_now + 1
      q.append((nxt, time_now+1))


print(time[K])
