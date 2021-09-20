# 투 포인터
import math
N, S = map(int, input().split())
arr = []
for i in map(int, input().split()):
    arr.append(i)
    
sum_ = arr[0]
length = math.inf
low = 0
high = 0

while low <= high and high < N:
    if sum_ < S:
        high += 1
        if high == N:
            break
        sum_ += arr[high]
        
    elif sum_ == S:
        length = min(length, high-low+1)
        high += 1
        if high == N:
            break
        sum_ += arr[high]
        
    elif sum_ > S:
        length = min(length, high-low+1)
        sum_ -= arr[low]
        low += 1
        
if length == math.inf:
    print(0)
else:
    print(length)