import sys
from collections import deque

N = int(sys.stdin.readline())

inputs = []

for _ in range(N):
  ftns = sys.stdin.readline().rstrip()
  M = int(sys.stdin.readline())
  arr_string = sys.stdin.readline().rstrip()

  if arr_string == "[]":
    arr = deque([])
  else:
    arr = deque(list(map(int, arr_string[1:-1].split(','))))

  inputs.append((ftns, arr))

def solution(ftns, arr):
  isError = False
  stage = 1
  for ftn in ftns:
    if ftn == 'R':
      stage *= -1
    # ftn == 'D'
    elif arr and stage == 1:
      arr.popleft()
    elif arr and stage == -1:
      arr.pop()
    else:
      print("error")
      isError = True
      break

  if not isError:
    if stage == 1:
      print(str(list(arr)).replace(" ", ""))
    else:
      print(str(list(arr)[::-1]).replace(" ", ""))

for ftns, q in inputs:
  solution(ftns, q)