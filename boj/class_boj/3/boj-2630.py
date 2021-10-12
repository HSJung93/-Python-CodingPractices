import sys
n = int(sys.stdin.readline())

box = []

for _ in range(n):
  box.append(list(map(int, sys.stdin.readline().split())))

d = {"white": 0, "blue": 0}

def check(x, y, n):
  val = box[x][y]
  for i in range(n):
    for j in range(n):
      if box[x+i][y+j] != val:
        return False
  return True

def divide(x, y, n):

  if check(x, y, n):
    if box[x][y] == 0:
      d["white"] += 1
    else:
      d["blue"] += 1
  else:
    for i in range(2):
      for j in range(2):
        divide(x+i*n//2, y+j*n//2, n//2)

divide(0, 0, n)

print(d["white"])
print(d["blue"])