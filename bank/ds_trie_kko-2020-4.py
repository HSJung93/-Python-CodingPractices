def index(ch):
    return ord(ch) - ord('a')

SZ = 10000
AP = index('z') + 1

class Node:
    def __init__(self):
        self.nxt = [0] * AP
        self.cnt = 0

def build(words):
    trie = [Node() for _ in range(SZ+1)]
    for item in words:
        n = len(item)
        trie[n].cnt += 1
        floor = trie[n].nxt
        for i in range(n):
            idx = index(item[i])
            if floor[idx] == 0:
                floor[idx] = Node()
            floor[idx].cnt += 1
            floor = floor[idx].nxt
    return trie

def rev(words):
    rst = []
    for item in words:
        rst.append(item[::-1])
    return rst

def test(trie, item):
    n = len(item)
    floor = trie[n].nxt
    sz = trie[n].cnt
    for i in range(n):
        if item[i] == '?':
            return sz
        idx = index(item[i])
        if floor[idx] == 0:
            return 0 
        sz = floor[idx].cnt
        floor = floor[idx].nxt

def solution(words, queries):
    trieA = build(words)
    trieB = build(rev(words))
    print(trieA[5].cnt)
    print(trieA[5].nxt[5].cnt)
    answer = []
    for item in queries:
        if item[0] == '?' and item[-1] == '?':
            answer.append(trieA[len(item)].cnt)
        elif item[-1] == '?':
            answer.append(test(trieA, item))
        else:
            answer.append(test(trieB, item[::-1]))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))

"""
result:
[3, 2, 4, 1, 0]
"""