import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

number_name = defaultdict(str)
name_number = defaultdict(str)

for i in range(1, N+1):
  name = sys.stdin.readline().rstrip()
  number_name[str(i)] = name
  name_number[name] = str(i)

answer = []

for _ in range(M):
  question = sys.stdin.readline().rstrip()
  if question.isdigit():
    print(number_name[question])
  else:
    print(name_number[question])