def minPathSum(grid):
  m = len(grid)
  n = len(grid[0])
    
  dp = [[101] * n for _ in range(m)]
    
  for i in range(m):
    for j in range(n):
      if i == 0 and j == 0:
        dp[i][j] = grid[i][j]
        continue
      if i == 0:
        dp[i][j] = grid[i][j] + dp[i][j-1]
        print("!!")
        print(dp[i-1][j])
        print(grid[i][j])
        print(dp)
        continue
      if j == 0:
        dp[i][j] = grid[i][j] + dp[i-1][j]
        print(grid[i][j])
        print(dp[i][j-1])
        print("!!!")
        continue
      dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
      print(dp)
            
  return dp[m-1][n-1]
  
  
print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))