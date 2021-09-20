from collections import deque
import math

# 어느 순간 작업이 길어지면 함수로 뺀다.
def midx(n ,pi, pj, qi, qj):
    # 좌표계에서 두 좌표를 차지하는 위치를 기록하는 버전의 visited가 필요하다. 이차원 리스트로 구현하고 싶어서 한 좌표를 하나의 인덱스로 변형한다.
    pid = pi * n + pj
    qid = qi * n + qj
    # 다행히도 두좌표의 순서는 상관이 없다 따라서 하나만 기록한다. 
    if pid > qid :
        pid, qid = qid, pid
    return pid, qid

def isMarked(mk, n, pi, pj, qi, qj, t):
    pid, qid = midx(n, pi, pj, qi, qj)
    return mk[pid][qid] <= t

def mark(mk, n, pi, pj, qi, qj, t):
    pid, qid = midx(n, pi, pj, qi, qj)
    # 작은 값 기록도 함수 안에 넣어버린다. 어차피 동일하게 수행하기 때문
    mk[pid][qid] = min(mk[pid][qid], t)

def solution(board):
    n = len(board)
    mk = [[math.inf] * (n*n) for _ in range(n*n)]
    q = deque()
    q.append((0 ,0, 0, 1, 0))
    # 하나의 자료형을 만들면 전체에서 관련된 작업을 해준다.
    mark(mk, n, 0, 0, 0, 1, 0)
    
    rst = [[math.inf] * n for _ in range(n)]
    rst[0][0] = 0
    rst[0][1] = 0
    
    while q:
        pi, pj, qi, qj, t = q.popleft()
                    
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tpi, tpj, tqi, tqj = pi + di, pj + dj, qi + di, qj + dj
            if 0<=tpi<n and 0<=tpj<n and 0<=tqi<n and 0<=tqj<n:
                if board[tpi][tpj] == 0 and board[tqi][tqj] == 0:
                    if not isMarked(mk, n, tpi, tpj, tqi, tqj, t+1):
                        rst[tpi][tpj]= min(rst[tpi][tpj], t+1)
                        rst[tqi][tqj] = min(rst[tqi][tqj], t+1)
                        mark(mk, n, tpi, tpj, tqi, tqj, t+1)
                        q.append((tpi, tpj, tqi, tqj, t+1))      
    
        for npi, npj, nqi, nqj, r in [(pi, pj, qi, qj, 1), (pi, pj, qi, qj, -1), (qi, qj, pi, pj, 1), (qi, qj, pi, pj, -1)]:
            
                    
            di, dj = nqi - npi, nqj - npj
            tpi, tpj, tqi, tqj = npi, npj, nqi, nqj
            
            if di == 0 and dj == 1:
                tpi += r
                tqi += r
            elif di == 1 and dj == 0:
                tpj -= r
                tqj -= r
            elif di == 0 and dj == 0:
                tpi -= r
                tqi -= r
            elif di == -1 and dj == 0:
                tpj += r
                tqj += r
            if 0<=tpi<n and 0<=tpj<n and 0<=tqi<n and 0<=tqj<n:
                if board[tpi][tpj] == 0 and board[tqi][tqj] == 0:
                    tpi, tpj = npi, npj
                    if di == 0 and dj == 1:
                        tqi = tpi + r
                        tqj = tpj
                    elif di == 1 and dj == 0:
                        tqi = tpi
                        tqj = tpj - r
                    elif di == 0 and dj == 0:
                        tqi = tpi - r
                        tqj = tpj
                    elif di == -1 and dj == 0:
                        tqi = tpi
                        tqj = tpj + r
                    if not isMarked(mk, n, tpi, tpj, tqi, tqj, t+1):
                            rst[tqi][tqj] = min(rst[tqi][tqj], t+1)
                            mark(mk, n, tpi, tpj, tqi, tqj, t+1)
                            q.append((tpi, tpj, tqi, tqj, t+1)) 
                

        # 8 cases
        # calc test index
        # test
        
        # calc move index
        
        # check marked
        # update rst
        # mark 
        # append q
    answer = rst[n-1][n-1]
    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

print(solution(board))

"""
output:
7
"""