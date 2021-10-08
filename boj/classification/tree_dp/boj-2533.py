import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
  fr, to = map(int, sys.stdin.readline().split())
  graph[fr].append(to)
  graph[to].append(fr)

# 얼리 x 일때 얼리의 갯수 값, 얼리 일때 얼리의 갯수 값. 노드별로 리스트
dp = [[0, 0] for _ in range(N+1)]

def dfs_dp(num):
  # 그래서 자식 노드가 없는 끝 노드의 경우 값
  visited[num] = True
  dp[num][0] = 0
  dp[num][1] = 1

  # 다음이 없으면 오류 없이 안 돌아감
  for nxt in graph[num]:
    if not visited[nxt]:
      dfs_dp(nxt)
      # 다음 노드의 값이 계산되었다. 이번 노드의 값을 계산한다. 
      # 여러 자식 노드에 대하여 합으로 계산된다. 
      dp[num][0] += dp[nxt][1]
      dp[num][1] += min(dp[nxt][0], dp[nxt][1])

# 한 노드로부터 시작해서
dfs_dp(1)
print(min(dp[1][0], dp[1][1]))