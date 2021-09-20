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
    result[matrix[start_x][start_y] + 1] += 1 
  else: 
    for i in range(3): 
      for j in range(3): 
        divide(start_x + i* n//3, start_y + j* n//3, n//3) 
  
  return 

divide(0, 0, N) 

for i in range(3): 
  print(result[i])
