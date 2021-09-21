import sys, copy, math
from itertools import permutations
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# board = []
# for i in range(5):
#   table = []
#   for i in range(5):
#     table.append(list(map(int, sys.stdin.readline().split())))
#   board.append(table)

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
visited_num = 0
answer = math.inf

def solve():
  for order in permutations(range(5), 5):
    stack_board(order, 0)
  print(answer if answer != math.inf else -1)
  
# ! make permutations and conclusion condition
def stack_board(order, idx):
  global board
  if answer == 12:
    return
  
  # spin boards
  if idx == 5:
    simul(order)
    return
  for _ in range(4):
    board_rotate(order[idx])
    stack_board(order, idx+1)
    
def simul(order):
  
  global answer, visited, visited_num 
  
  # make boards according to permutations
  game_board = []
  for idx in order:
    game_board.append(board[idx])
    
  visited_num += 1
  
  if game_board[0][0][0] != 1 or game_board[4][4][4] != 1:
    return
  
  visited_num += 1
  q = deque([[0,0,0,0]])
  visited[0][0][0] = visited_num

  while q:
    # dfs
    z, x, y, cnt = q.pop()
    
    # 쓸모없는 탐색을 하지 않는다.
    if cnt >= answer:
      continue
    
    if 4 == z and 4 == x and 4 == y:
      answer = min(answer, cnt) 
      break
    
    for i in range(6):
      nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
      
      if isValid(nz, nx, ny, game_board):
        visited[nz][nx][ny] = visited_num
        q.appendleft((nz, nx, ny, cnt+1))
        
def isValid(z, x, y, game_board):
  if z < 0 or x < 0 or y < 0 or z >= 5 or x >= 5 or y >= 5:
    return False
  elif game_board[z][x][y] == 0:
    return False
  elif visited[z][x][y] == visited_num:
    return False
  return True

def board_rotate(z):
  
  global board
  
  tmp = copy.deepcopy(board[z])
  
  for i in range(5):
    for j in range(5):
      board[z][j][4-i] = tmp[i][j]

solve()