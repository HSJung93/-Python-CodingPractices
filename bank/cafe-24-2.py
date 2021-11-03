def calc(string):
    count = 0
    d = {'3': True, '6': True, '9': True}
    for char in string:
        if char in d:
            count += 1
    return count

def solution(param):
    answer = 0
    for i in range(1, param+1):
        answer += calc(str(i))
        print(calc(str(i)))
    return answer


print(solution(35))