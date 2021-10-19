from itertools import combinations
from collections import deque
import math, heapq

def do(typ, r1, c1, r2, c2, degree):
    # 높힌다
    if typ == 1:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] -= degree
    # 낮춘다
    else:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += degree

def solution(board, skill):
    
    for typ, r1, c1, r2, c2, degree in skill:
        do(typ, r1, c1, r2, c2, degree)
        
    cnt = 0
      
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1
    
    return cnt

# input
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))

"""
result:
10
"""