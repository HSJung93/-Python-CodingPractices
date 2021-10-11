import sys
n, r, c = map(int, sys.stdin.readline().split())

num = 0

while n > 0:
  temp = (2**n)//2
  if n > 1:
    if r < temp and c >= temp:
      num += temp**2
      c -= temp
    elif r >= temp and c < temp:
      num += (temp**2) * 2
      r -= temp
    elif r >= temp and c >= temp:
      num += (temp**2) * 3
      r -= temp
      c-= temp
  elif n == 1:
    if r == 0 and c == 1:
      num += 1
    elif r == 1 and c == 0:
      num += 2
    elif r == 1 and c == 1:
      num += 3
  n -= 1
  
print(num)