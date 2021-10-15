import math
M, N = map(int, input().split())

def printDecimal(i):
    notDecimal = False
    for j in range(2, math.ceil(math.sqrt(i) + 1)):
        if i%j == 0:
            notDecimal = True
            break 
            
    if notDecimal == False:
        print(i)

for i in range(M, N+1):
    printDecimal(i)