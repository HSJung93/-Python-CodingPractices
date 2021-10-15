def combinationSum(candidates, target):
  res = []
  def dfs(csum, index, path):
    print(csum, index, path)
    if csum < 0:
      return
    if csum == 0:
      res.append(path)
      return
    for i in range(index, len(candidates)):
      dfs(csum-candidates[i], 0, path+[candidates[i]])
      
  dfs(target, 0, [])
  return res

print(combinationSum([1,1,1,1], 5))