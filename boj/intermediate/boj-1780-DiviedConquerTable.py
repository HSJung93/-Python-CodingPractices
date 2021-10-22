import sys 

N = int(sys.stdin.readline()) 
matrix = [] 
result = [0] * 3 

# index 0 1 2
# value -1 0 1

for _ in range(N): 
  matrix.append(list(map(int, sys.stdin.readline().split()))) 
    
def check(start_x, start_y, n): 
  temp = matrix[start_x][start_y] 
  for i in range(n): 
    for j in range(n): 
      if temp != matrix[start_x + i][start_y + j]: 
        return False 
  
  return True 
    
def divide(start_x, start_y, n): 
  if check(start_x, start_y, n): 
    # 외부 변수를 업데이트하는 동작으로 구현하는 것이 편한 경우가 많다.
    # 1 -> 2번째 값을
    # 0 -> 1번째 값을
    # -1 -> 0번째 값을
    result[matrix[start_x][start_y] + 1] += 1 
  else: 
    for i in range(3): 
      for j in range(3): 
        divide(start_x + i* n//3, start_y + j* n//3, n//3) 
  
  # divide conquer는 내부에 재귀를 돌려 외부 변수를 업데이트를 하게 한 뒤에 마지막에 ret만 하여 종결.
  return 

divide(0, 0, N) 

for i in range(3): 
  print(result[i])


"""
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1

10
12
11
"""