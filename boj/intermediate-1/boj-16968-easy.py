import sys
s = sys.stdin.readline().rstrip()

ans = 1
prev = ""
for char in s:
  
  if prev == char:
    if char == 'c':
      ans *= 25
    else:
      ans *= 9
  
  else:
    if char == 'c':
      ans *= 26
    else:
      ans *= 10
      
  prev = char
      
    
print(ans)