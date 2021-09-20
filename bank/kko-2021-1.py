from itertools import combinations
from collections import deque, defaultdict
import math, heapq


def solution(id_list, report, k):
    
    rep = defaultdict(list)
    user_rep = defaultdict(list)
    for string in list(set(report)):
        fr, to = string.split()
        rep[to].append(fr)
        user_rep[fr].append(to)
        
    ban = []
    for key in rep.keys():
        if len(rep[key]) >= k:
            ban.append(key)
            
    ret = []
    for id in id_list:
        ret.append(len(set(user_rep[id]) & set(ban)))
    
    return ret

# input

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))

"""
result:
[2,1,1,0]

"""