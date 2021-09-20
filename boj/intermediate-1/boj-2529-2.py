n = int(input())
arr = input().split()
visited = [False for i in range(10)]
mn,mx = '', ''

def check(i,j,test):
  if test == '<':
    return i<j
  else:
    return i>j

# 체크하면서 탐색하고 싶은 배열 text를 변수로 넣어 재귀 함수에서 업데이트
def dfs(cnt, text):
  print(text)

  global mn
  global mx

  # 최소값은 가장 먼저 만들어진 수, 최대값은 나중에 만들어진 수
  if cnt == n+1:
    if len(mn) == 0:
      mn = text
    else:
      mx = text
    return
  
  # 같은 길이중에서 조건을 만족하는 경우를 체크한다. 
  for i in range(10):
    if visited[i] == False:
      if cnt == 0 or check(int(text[-1]), i, arr[cnt-1]):
        visited[i] = True
        # 길이를 늘린다.
        dfs(cnt+1, text+str(i))
        # 재귀 함수를 빠져나오면 방문을 취소해서 다음 루프에서 다시 방문 할 수 있도록 한다. 
        visited[i] = False

dfs(0, "")
print(mx)
print(mn)
    
