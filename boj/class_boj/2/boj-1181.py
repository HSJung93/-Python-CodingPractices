"""
문제: 정렬 1. 길이 짧은 순 2. 알파벳 순

입력:
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

출력:
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate

ctl + ` 로 터미널 이동
"""

import sys
N = int(sys.stdin.readline())
a = []
for _ in range(N):
  a.append(sys.stdin.readline().rstrip())

a = set(a)
a = list(a)
a.sort()
a.sort(key=len)

for s in a:
  print(s)
