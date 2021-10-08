from collections import defaultdict

def canSum(target, num_list, memo):
    if target in memo: return memo[target]
    if target == 0: return True
    if target <0: return False
    
    for num in num_list:
        remainder = target - num
        if canSum(remainder, num_list, memo):
            memo[target] = True
            return True
        
    memo[target] = False
    return False

memo = defaultdict(bool)
print(canSum(7, [2, 3], memo))
memo = defaultdict(bool)
print(canSum(7, [5, 3, 4, 7], memo))
memo = defaultdict(bool)
print(canSum(7, [2, 4], memo))
memo = defaultdict(bool)
print(canSum(8, [2, 3, 5], memo))
memo = defaultdict(bool)
print(canSum(300, [7, 14], memo))



        
    