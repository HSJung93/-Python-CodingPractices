def whirl(rowStart, rowEnd, colStart, colEnd, cnt, arr):
  for j in range(colStart, colEnd):
    arr[rowStart][j] = cnt
    cnt += 1
  
  rowStart += 1
  
  if rowStart >= rowEnd:
    return

  for i in range(rowStart, rowEnd):
    arr[i][colEnd-1] = cnt
    cnt += 1
    
  colEnd -= 1
  
  for j in range(colEnd-1, colStart-1, -1):
    arr[rowEnd-1][j] = cnt 
    cnt += 1
    
  rowEnd -= 1
  
  if colStart >= colEnd:
    return

  for i in range(rowEnd-1, rowStart-1, -1):
    arr[i][colStart] = cnt
    cnt += 1
    
  colStart += 1
  
  whirl(rowStart, rowEnd, colStart, colEnd, cnt, arr)


def makeSnail(N):

  arr = [[0]*N for _ in range(N)]
  rowStart, rowEnd, colStart, colEnd= 0, N, 0, N
  cnt = 0
  whirl(rowStart, rowEnd, colStart, colEnd, cnt, arr)
  
  return arr

def mergeSnail(snailOne, snailTwo):
  
  arr0 = snailOne 
  arr1 = snailTwo 
  n0, n1 = len(arr0), len(arr1)
  M = n0*n1
  
  arr = [[0]*M for _ in range(M)]
  for i in range(M):
    for j in range(M):
      arr[i][j] += arr1[i%n1][j%n1]
      arr[i][j] += arr0[i//n1][j//n1]*n1*n1
      
  return arr

def makeSnails(nums):
  
  snailOne = makeSnail(nums[0])
  
  for i in range(1, len(nums)):
    snailOne = mergeSnail(snailOne, makeSnail(nums[i]))
    
  return snailOne

for ar in makeSnails([2, 2, 2]):
  print(ar)