# f11 1
# f21 1
# f12 1
# f22 2
# f23 3
# f32 3
# f33 f23 + f22 + f21 3+ 2+ 1 =6

# 1 1 1 1 1 1 1
# 1 2 3
# 1 3 6
# 1
# 1
# 1
# 1
# f(m, n) = f(m-1, n) + f(m-1, n-1) + f(m-1, n-2)
# = f(m-1, n) + f(m, n-1)

# import sys
# sys.setrecursionlimit(10000)


def gridTraveler(m, n, memo):
    if memo[m][n] != -1: 
        return memo[m][n]
    if m == 1 and n == 1: 
        return 1
    if m == 0 or n == 0: 
        return 0
    memo[m][n] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[m][n]

m, n = 30, 30

memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]

print(gridTraveler(m, n, memo))


