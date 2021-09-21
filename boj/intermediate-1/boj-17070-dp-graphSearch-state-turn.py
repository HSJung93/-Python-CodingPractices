import sys

N = int(sys.stdin.readline().strip())
table = []

for _ in range(N):
  table.append([int(x) for x in sys.stdin.readline().split()])

# 현재 방향 별로 갈 수 있는 다음 방향, 가로 0 세로 1 대각선 2
directions = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}

# 다음 방향에 가고 싶을 때 가게 될 좌표 좌표
cos = {0: [0, 1], 1: [1, 0], 2:[1, 1] }

# r 좌표 c 좌표 d 
dp = [[[ 0 for _ in range(3) ] for _ in range(N)] for _ in range(N)]

# 0, 1에 가로로 오는 경우의 수는 한가지다.
dp[0][1][0] = 1

def check(r, c, d):
  
  # 현재 놓여있는 방향에 따라서 갈 수 있는 방향만 나옴
  for direction in directions[d]:
    dr, dc = cos[direction]
    nr = r + dr
    nc = c + dc
    
    # 가로 세로 갈때와 대각선 갈때 모두 갈 좌표가 갈 수 있어야 한다.
    if 0 <= nr < N and 0 <= nc < N and not table[nr][nc]:
      if direction != 2:
        dp[nr][nc][direction] += dp[r][c][d]
      else:
        
        # 대각으로 움직일 경우 가로와 세로를 둘다 확인해야함(생각보다 간단함)
        if not table[nr-1][nc] and not table[nr][nc-1]:
          dp[nr][nc][direction] += dp[r][c][d]
        
    
for r in range(N):
  for c in range(N):
    for d in range(3):
      if dp[r][c][d] and not table[r][c]:
        check(r, c, d)
        
print(sum(dp[N-1][N-1]))
    
"""
3
0 0 0
0 0 0
0 0 0

1

4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

3

5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

0

6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

13

"""