
def LIS(myList):
    
    l = [1] * len(myList) # 높낮이를 기록
    elm = [0] * len(myList) # 비교되는 이전 인덱스를 기록
    
    for i in range(1, len(myList)):
        for j in range(0, i):
            # myList가 인덱스가 증가하는 두 수를 비교 했을 때 증가하고 l은 같거나 작으면 뒤의 l을 증가시킨다. 
            if myList[i] > myList[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
                elm[i]= j
                print("l")
                print(l)
                print("elm")
                print(elm)
                
    idx = 0
    
    maximum = max(l)
    idx = l.index(maximum)
    
    seq = [myList[idx]]
    while idx != elm[idx]:
        idx = elm[idx]
        seq.append(myList[idx])
        
    return (maximum, reversed(seq))

myList = [10, 22, 9, 33, 21, 50, 41, 60]
ans = LIS(myList)
print ('Length of lis is', ans[0])
print ('The longest sequence is', ', '.join(str(x) for x in ans[1]))