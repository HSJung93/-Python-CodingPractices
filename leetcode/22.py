from typing import List

def generateParenthesis(n: int) -> List[str]:
  if n == 0:
    return []
        
  res = []
        
  generate(res, "", n, n)
  return res
    
def generate(res, s, left, right):
  print(res, s, left, right)
  if left > right:
    return
        
  if left == 0 and right == 0:
    res.append(s)
    return
        
  if left > 0:
    generate(res, s + "(", left - 1, right)
            
  if right > 0:
    generate(res, s + ")", left, right - 1)
        
print(generateParenthesis(3))