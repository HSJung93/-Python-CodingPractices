import sys, math

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def isPrime(number):
  if number == 1:
    return False
  elif number == 2:
    return True
  for i in range(2, int(math.sqrt(number))+1):
    if number % i == 0:
      return False
  
  return True

count = 0

for number in arr:
  if isPrime(number):
    count += 1

print(count)