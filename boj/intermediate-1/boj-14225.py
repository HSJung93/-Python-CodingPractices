import sys
N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

MAX = N*max(S) + 2

sum_list = [0] * MAX

def dfs(i, num):
  if i == N:
    return

  sum_list[num+S[i]] = 1
  dfs(i+1, num+S[i])
  dfs(i+1, num) 

dfs(0, 0)

for i in range(1, MAX):
  if sum_list[i] == 0:
    print(i)
    break
  
