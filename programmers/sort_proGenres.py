from collections import defaultdict

def solution(genres, plays):
    l = len(genres)
    
    genres_count = defaultdict(int)
    
    for i in range(l):
        genres_count[genres[i]] += plays[i]
        
    genres_order_list = list(dict(sorted(genres_count.items(), key = lambda x:x[1], reverse=True)).keys())
    genres_order_map = {key: i for i, key in enumerate(genres_order_list)}
    
    d = []
    
    for g, p, i in zip(genres, plays, range(l)):
        d.append((g, p, i))
        
    d.sort(key=lambda x: x[1], reverse=True)
    d.sort(key=lambda d: genres_order_map[d[0]])

    
    name = ""
    cnt = 0
    answer = []
    
    for g, p, i in d:
        if name == g:
            cnt += 1
            if cnt >= 2:
                continue
        else:
            cnt = 0
        name = g
        answer.append(i)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]	))