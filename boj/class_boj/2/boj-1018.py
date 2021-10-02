import sys, math

Eight = 8
N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
  graph.append(list(sys.stdin.readline().rstrip()))
  
wstrings = ["WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW"]

wgraph = []
for i in range(8):
  wgraph.append(list(wstrings[i]))

bstrings = ["BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB"]

bgraph = []
for i in range(8):
  bgraph.append(list(bstrings[i]))
  
def calc(i, j):
  wcount = 0
  bcount = 0
  for di in range(Eight):
    for dj in range(Eight):
      if graph[i+di][j+dj] != wgraph[di][dj]:
        wcount += 1
      if graph[i+di][j+dj] != bgraph[di][dj]:
        bcount += 1
    
  return min(wcount, bcount)
  
  
min_paint = math.inf
for i in range(N-Eight+1):
  for j in range(M-Eight+1):
    # i 부터 i +7
    min_paint = min(min_paint, calc(i, j))
    
print(min_paint)


"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

1

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

12
"""