from itertools import combinations
from collections import deque
import math, heapq


def solution(leave, day, holidays):
    answer = -1
    # 0일의 값은 나중에 제거
    calendar = [1] * 31
    
    days = {"SUN":0, "MON":6, "TUE":5, "WEN":4, "THU":3, "FRI":2, "SAT":1}
    
    free = days[day]
    
    for i in range(31):
        if i % 7 == free or i % 7 == ((free + 1)% 7):
            calendar[i] = 0
    
    for i in holidays:
        calendar[i] = 0
        
    # 29 까지
    cal = calendar[1:]
    sm = 0
    mx = 0
    
    for i in range(len(cal)-1):
        sm = cal[i]
        for j in range(i+1, len(cal)):
            sm += cal[j]
            # 개선 가능
            if sm <= leave:

                mx = max(mx, j-i+1)
            else:
              break
            
    return mx


print(solution(4, "FRI", [3, 13, 15, 17]))


"""
result:


"""