from itertools import combinations
from collections import deque
import math, heapq


def solution(student, k):
    
    n = len(student) # 데이터의 개수 N
    m = k # 찾고자 하는 부분합 M
    data = student # 전체 수열

    count = 0
    interval_sum = 0
    end = 0

    # start를 차례대로 증가시키며 반복
    for start in range(n):
        end = start
        interval_sum = 0
        while interval_sum <= m and end < n:

            interval_sum += data[end]
            if interval_sum == m:
                count += 1
            end += 1

            
        # 부분합이 m일 때 카운트 증가
        
        interval_sum -= data[start]

    return count

# input

print(solution([0,1,0,0], 	1))
print(solution([0, 1, 0, 0, 1, 1, 0], 2))
print(solution([0, 1, 0], 	2))


"""
result:



"""