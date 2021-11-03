def convert(idx, n):
    # 00 01 02 
    # 03 13 23 
    # 33 32 31
    # 30 20 10
    x = 0
    y = 0
    x_min = 0
    x_max = n
    y_min = 0
    y_max = n

    while idx >0:
        for _ in range(y_max-y_min):
            y += 1
            idx -= 1
            if idx == 0:
                return [x, y]
        x_min += 1
        for _ in range(x_max-x_min):
            x += 1
            idx -= 1
            if idx == 0:
                return [x, y]
        y_max -= 1
        for _ in range(y_max-y_min):
            y -= 1
            idx -= 1
            if idx == 0:
                return [x, y]
        x_max -= 1
        for _ in range(x_max-x_min):
            x -= 1
            idx -= 1
            if idx == 0:
                return [x, y]
        y_min += 1
               
    return [x, y]

def solution(n, jump):
    answer = []
    arr = [0] * (n ** 2)
    arr[0] = 1
    idx = 0
    while 0 in arr:
        idx = (idx + jump) % (n**2)
        if arr[idx] == 1:
            while arr[idx] == 1:
                idx = (idx + 1) % (n**2)
        arr[idx] = 1
        
    answer = convert(idx, n)
    
    return answer

print(solution(5, 1))