def solution(tickets):
    answer = []
    s = []
    s_ = []
    for ticket in tickets:
        if ticket[0] == "ICN":
            s_.append(ticket)
    s_.sort(key= lambda x : x[1])
    s.append(s_[0])
    
    while s:

        done = s.pop(0)
        next = done[1]
        answer.append(done[0])
        tickets.remove(done)
        if len(tickets) < 1:
            answer.append(done[1])
            break
        
        s_ = []
        for ticket in tickets:
            if ticket[0] == next:
                s_.append(ticket)
        if len(s_) ==0:
            break
        s_.sort(key=lambda x : x[1])
        s.append(s_[0])
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))