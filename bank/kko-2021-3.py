from itertools import combinations
from collections import deque, defaultdict
import math, heapq

def decode(s):
    H, M = map(int, s.split(':'))
    return H * 60 + M

def solution(fees, records):
    
    s = defaultdict()
    
    pay = defaultdict(int)
    
    for re in records:
        time, name, inOut = re.split()
        
        # print(s)
        
        if inOut == 'IN':
            s[name] = time
        else:
            # print(f"time{time}")
            # print(f"sname{s[name]}")
            # print(f"{decode(time) - decode(s[name])}")
            pay[name] += decode(time) - decode(s[name])
            del(s[name])
               
    for left_name in s.keys():
        pay[left_name] += decode('23:59') - decode(s[left_name])     
    
    srt = sorted(pay.items(), key= lambda x: x[0])
    
    
    rst = []
    
    basic_time, basic_fee, unit, unit_fee = fees

    for x, t in srt:
        rst.append(calc(t, basic_time, basic_fee, unit, unit_fee))
        
    return rst

def calc(t, basic_time, basic_fee, unit, unit_fee):
    if t <= basic_time:
        return basic_fee
    return basic_fee + math.ceil((t-basic_time)/unit) * unit_fee

# input
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))



"""
result:



"""