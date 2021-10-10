from collections import defaultdict

a = []

for i in range(1, 22, 5):
  b = []
  for j in range(5):
    b.append(i+j)
    
  a.append(b)
  
for ar in a:
  print(ar)

print()

qs= [ [2, 2, 5, 4, 1],  [2, 2, 5, 4, 1], [1, 3, 4, 5, -1]]

def flipA(r1, c1, r2, c2):
  
  global a
  
  d = defaultdict(list)
  for r in range(r1, r2+1):
    for c in range(c1, c2+1):
      d[r+c].append(a[r][c])
      
  indexs_list = []
      
  for c in range(c1, c2+1):
    indexs_list.append((r1, c))
    
  for r in range(r1+1, r2+1):
    indexs_list.append((r, c2))
      
  # 0 1 2 3 4 5
  for indexs, k in zip(indexs_list, d.keys()):
    r0, c0 = indexs 
    for val in d[k][::-1]:
      a[r0][c0] = val
      r0 += 1
      c0 -= 1

def flipB(r1, c1, r2, c2):
  
  global a
  
  d = defaultdict(list)
  for r in range(r1, r2+1):
    for c in range(c2, c1-1, -1):
      d[r-c].append(a[r][c])
      
  indexs_list = []
      
  for c in range(c2, c1-1, -1):
    indexs_list.append((r1, c))
    
  for r in range(r1+1, r2+1):
    indexs_list.append((r, c1))
      
  # 0 1 2 3 4 5
  for indexs, k in zip(indexs_list, d.keys()):
    r0, c0 = indexs 
    for val in d[k][::-1]:
      a[r0][c0] = val
      r0 += 1
      c0 += 1

def solution(a, qs):
  
  for r1, c1, r2, c2, typ in qs:
    if typ == 1:
      flipA(r1-1, c1-1, r2-1, c2-1)
    else:
      flipB(r1-1, c1-1, r2-1, c2-1)
      
    for ar in a:
      print(ar)
    print()
      
  return a

solution(a, qs)

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
# [21, 22, 23, 24, 25]

# [1, 2, 3, 4, 5]
# [6, 7, 12, 17, 10]
# [11, 8, 13, 22, 15]
# [16, 9, 18, 23, 20]
# [21, 14, 19, 24, 25]

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
# [21, 22, 23, 24, 25]

# [1, 2, 15, 10, 5]
# [6, 7, 20, 9, 4]
# [11, 12, 19, 14, 3]
# [16, 17, 18, 13, 8]
# [21, 22, 23, 24, 25]