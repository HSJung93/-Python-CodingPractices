import sys
N = int(sys.stdin.readline())

s = [0] * (20 + 1)

for _ in range(N):
  input_string = sys.stdin.readline()
  if input_string[:2] == "al":
    s = [1] * (20 + 1)
  elif input_string[0] == "e":
    s = [0] * (20 + 1)
  else:
    order, number = input_string.split()
    number = int(number) 
    if order == "add":
      if not s[number]:
        s[number] = 1
    elif order == "check":
      if s[number]:
        print(1)
      else:
        print(0)
    elif order == "remove":
      if s[number]:
        s[number] = 0
    elif order == "toggle":
      if s[number]:
        s[number] = 0
      else:
        s[number] = 1
