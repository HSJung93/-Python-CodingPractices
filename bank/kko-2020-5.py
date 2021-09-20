def testB(pillar, bar, x, y, N):
    if y-1 >= 0 and pillar[x][y-1] == 1:
        return True
    if x+1 < N and y-1 >= 0 and pillar[x+1][y-1] == 1:
        return True
    if x-1 >= 0 and x+ 1 < N and bar[x-1][y] == 1 and bar[x+1][y] == 1:
        return True
    return False
        
def testP(pillar, bar, x, y):
    if y == 0:
        return True
    if x-1 >= 0 and bar[x-1][y] == 1:
        return True
    if bar[x][y] == 1:
        return True
    if y-1 >= 0 and pillar[x][y-1] == 1:
        return True
    return False
    
def solution(n, build_frame):
    N = n+1
    bar = [[0] * N for _ in range(N)]
    pillar = [[0] * N for _ in range(N)]
    # 보와 기둥 만들기
    for x, y, a, b in build_frame:
        
        # 설치
        if b == 1:
            # 기둥 설치
            if a == 0:
                if testP(pillar, bar, x, y):
                    pillar[x][y] = 1
                
            # 보 설치 a == 1
            else:
                if testB(pillar, bar, x, y, N):
                    bar[x][y] = 1
                       
        # 삭제 b == 0
        else:
            # 기둥 삭제
            if a == 0:
                pillar[x][y] = 0
                test = True
                for i in range(N):
                    for j in range(N):
                        test &= bar[i][j] == 0 or testB(pillar, bar, i, j, N)
                        test &= pillar[i][j] == 0 or testP(pillar, bar, i, j)
                if test is False:
                    pillar[x][y] = 1
                
            # 보 삭제 a == 1
            else:      
                bar[x][y] = 0
                test = True
                for i in range(N):
                    for j in range(N):
                        test &= bar[i][j] == 0 or testB(pillar, bar, i, j, N)
                        test &= pillar[i][j] == 0 or testP(pillar, bar, i, j)                
                if test is False:
                    bar[x][y] = 1      
            
            
    answer = []
    for i in range(N):
        for j in range(N):
            if pillar[i][j] == 1:
                answer.append([i, j, 0])
            if bar[i][j] == 1:
                answer.append([i, j, 1])
    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))

"""
result:
[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

result:
[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
"""