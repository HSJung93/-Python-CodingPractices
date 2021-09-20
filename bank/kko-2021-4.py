from itertools import permutations, combinations
from collections import deque
import math, heapq

# n = 10
def decompose(n):
    s = deque([n])
    rst = []
    while s:
        rst.append(list(s))
        a = s.pop()
        if a != 1:
            s.append(a-1)
            s.append(1)
        else:
            sum = 2
            while s and s[-1] == 1:
                s.pop()
                sum += 1
            if not s:
                break
            pivot = s.pop() - 1
            s.append(pivot)
            while(sum>pivot):
                s.append(pivot)
                sum -= pivot
                
            s.append(sum)
    return rst

def solution(n, info):
    comb = decompose(n)
    print(comb)
    rian = [0] * 11
    
    max_list = [-1]
    max_diff = 0
    
    comb = [[2, 2, 1]]
    
    for c in comb:
        for index_list in list(permutations(range(11), len(c))):
            print(index_list)
            for key, val in zip(index_list, c):
                rian[key] = val
            print(rian)
            diff = calc(info, rian)
            # 라이언 이김
            if diff >0 :
                if max_diff <= diff:
                    max_diff = diff
                    max_list = rian
                
            rian = [0] * 11
            
    return max_list

def calc(info, rian):
    info_score = 0
    rian_score = 0
    for i in range(11):
        if info[i] == 0 and rian[i] == 0:
            continue
        if info[i] < rian[i]:
            rian_score += 10 - i
        else:
            info_score += 10 - i
            
    return rian_score - info_score
            
# input
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n, info))

"""
result:



"""