from itertools import combinations
from collections import deque, Counter, defaultdict
import math, heapq


def solution(research, n, k):
    answer = None
    table = [[0] * len(research) for _ in range(26)]
    for i, r in enumerate(research):
        for alpha, num in dict(Counter(r)).items():
            table[ord(alpha) - 97][i] += num
            
    issue = []
    # defaultdict(int)
    for i in range(len(table)):
        
        dayCount = 0
        daySum = 0
        
        for j in range(len(table[0])):
            
            if table[i][j] >= k:
                dayCount += 1
                daySum += table[i][j]
                
            else:
                if dayCount 
                if daySum >= 2 * n * k:
                    for _ in range(dayCount):
                        issue.append(chr(i+97))
                
                dayCount = 0
                daySum = 0
                    
                
                
    print(issue)
                
    if len(issue) == 0:
        return None
    # issue.sort()
    answer = Counter(issue).most_common()[0][0]  
              
    return answer

# input

# print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"], 2, 2))
print(solution(["yxxy","xxyyy"], 2, 1))
# print(solution(["yxxy","xxyyy","yz"], 2, 1))
# print(solution(["xy","xy"], 1, 1))

"""
result:
"a"
"x"
"y"
"None"
"""