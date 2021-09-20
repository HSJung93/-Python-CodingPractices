from itertools import combinations
from collections import deque
import math, heapq

def conv(x, y):
    if y == 0:
        return str(x)
    
    s = ''
    t = '0123456789ABCDEF'
    while x > 0:
        s += t[int(x % y)]
        x = int(x//y)
    s = s[::-1]
    return s

def isPrime(string):
    num = int(string)
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def noZero(string):
    for char in string:
        if char == "0":
            return False
    return True
    
def check(string):
    return isPrime(string) and noZero(string) and not string == '1'
    
def solution(n, k):
    changed = conv(n, k)
    
    cnt = 0
    
    divided_by_zero = list(x for x in changed.split('0') if x != "")
    
    # print(divided_by_zero)
    
    for string in divided_by_zero:
        if check(string):
            cnt += 1
    
    # cnt = 0
    # for i in range(len(changed)):
    #     for j in range(i+1, len(changed)+1):
    #         if check(changed[i:j]):
    #             cnt += 1

    return cnt

# input
n = 437674
k = 3
print(solution(n, k))
n = 110011
k = 10
print(solution(n, k))

"""
result:
3


"""