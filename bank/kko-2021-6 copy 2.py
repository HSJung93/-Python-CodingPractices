from itertools import combinations
from collections import deque
import math, heapq
                    
def midx(n, i, j):
    id = i * n + j
    return id

def solution(board, skill):
    
    N = len(board[0])
    
    id_list = [0] * len(board) * len(board[0])
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            id_list[midx(N, i, j)] = board[i][j]
            
    # r1 ~ r2 + degree
    # ~(c1~c2) - degree
            
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    id_list[midx(N, i, j)] -= degree
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    id_list[midx(N, i, j)] += degree
        
    cnt = 0
      
    for i in range(len(id_list)):
        if id_list[i] > 0:
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