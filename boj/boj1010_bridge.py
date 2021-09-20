

"""
1. 콤비네이션의 수를 확인하는 함수를 직접 만들때
2. facto 메모이제이션 위치 

input:
3
2 2
1 5
13 29

output:
1
5
67863915
"""

import sys

def facto(x, m):
    if x in m:
        return m[x]
    if x == 0 or x == 1:
        return 1
    else:
        m[x] = x * facto(x-1, m)
        return m[x]

def combi(n, r):
    return int(facto(n, m) / (facto(r, m) * facto(n-r, m)))

rets = []
for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    rets.append(combi(M, N))
    
for ret in rets:
    print(ret)