
def solution(priorities, location):

    printed = [0]*len(priorities)
    idx = 0
    num = 1
    
    while num != len(priorities)+1:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            
        else:
            printed[idx%len(printed)] = num
            num += 1
            priorities.append(0)
        
        del priorities[0]    
        idx += 1
        
    return printed[location]

print(solution([1, 1, 9, 1, 1, 1], 0))


q를 사용하지 않고 list에 직접 돌려버린다.