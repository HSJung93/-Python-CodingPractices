import sys
string = sys.stdin.readline().rstrip()

res = ""
stack =[]

for char in string:
  if char.isalpha():
    res += char
  else:
    if char == "(":
      stack.append(char)
    elif char == "*" or char == "/":
      while stack and (stack[-1] == "*" or stack[-1] == "/"):
        res += stack.pop()
      stack.append(char)
    elif char == "+" or char == "-":
      while stack and stack[-1] != "(":
        res += stack.pop()
      stack.append(char)
    elif char == ")":
      while stack and stack[-1] != "(":
        res += stack.pop()
      stack.pop()

while stack:
  res += stack.pop()

print(res)