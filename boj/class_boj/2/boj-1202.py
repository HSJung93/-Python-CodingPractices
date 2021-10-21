import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

jew = []
for _ in range(N):
  heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))

bags = []
for _ in range(K):
  bags.append(int(sys.stdin.readline()))

# 용량이 작은 가방부터
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
  while jew and bag >= jew[0][0]:
    # tmp에 가벼운 보석의 가치를 -로 넣는다.
    heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])

  if tmp_jew:
    # temp의 값(가치)을 더한다.
    answer -= heapq.heappop(tmp_jew)
  elif not jew:
    break

print(answer)

