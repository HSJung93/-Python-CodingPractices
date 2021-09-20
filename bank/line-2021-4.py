from itertools import combinations
from collections import deque
import math, heapq

def getPrime(num):
    primes = []
    if num < 2:
        return primes
    for i in range(2, num+1):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
            elif j > i**0.5:
                break
        if isPrime:
            primes.append(i)
    return primes

def findP(n):
    for prime in sorted(getPrime(n)):
        if n%prime == 0:
            return prime
    return False

def union_arrays(arrays):
    l = []
    for arr in arrays:
        l.extend(arr)
      
    return l
        
    

def makeArray(input_array, p):
    if len(input_array) == 1:
        return input_array
    
    N = len(input_array) 
    array = []
    for i in range(p):
        array.extend([input_array[x-1] for x in range(1, N+1) if x % p == (i+1)%p])  
        
    recur_arrays = [] # n12 p=3 0-3 4-7 8-11
    # p 0 1 2 12//3 = 4
    # 0 :p-1 p: 2p-1  :Np
    # 0 -2 3- 5
    # N =6 p = 2
    # 0    1
    for i in range(p):
       recur_arrays.append(array[(N//p) * i : (N//p)*(i+1)-1])
    
    next_array = union_arrays(recur_arrays)
    makeArray(next_arrays, p)
    map(makeArray(p), recur_arrays)
        
    return 
    
        
def solution(n):
    p = findP(n)
    # input_array = [x for x in range(1, n+1)]
    test_array = [1, 3, 5, 7, 9, 11]
    answer = makeArray(test_array, p)
    print(answer)
    
    return

# input

print(solution(12))

"""
result:



"""