## 큐를 while문 안에서 for문으로 먼저 다 빼서 시간을 맞추는 방법

from collections import deque

def solution(conyPosition, brownPosition):
    time = 0
    MAX = 2 * 10**5 
    visit = [set() for _ in range(MAX+1)] # 브라운이 visit에 도달한 시간을 업데이트 해간다
    visit[brownPosition].add(0)
    q = deque()
    q.append((brownPosition, 0))
    
    cnt = 0
    
    while conyPosition <= MAX:
        conyPosition += time
        
        if conyPosition > MAX:
            return - 1
        
        if time in visit[conyPosition]: # 코니의 현 포지션에 브라운이 도착한 시간이 있다면 
            return time
        
        for i in range(0, len(q)):
            curPosition, curTime = q.popleft()
            # 값을 넣어두지 않으면 외부에 저장한 값에서 불러와야 하는데 외부에 저장한 값이 여러 개이기 때문에 불러오기가 쉽지 않다. 그래서 값을 저장해둔다. 
            newTime = curTime + 1
            
            for newPosition in (curPosition-1, curPosition+1, curPosition*2):
                if 0 <= newPosition <= MAX:
                    visit[newPosition].add(newTime)
                    q.append((newPosition, newTime))

        time += 1
        
print(solution(11, 2))
        