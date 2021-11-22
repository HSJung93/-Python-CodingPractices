import sys, math

# 3 1 7
# 3 2 5 4 7

def main():

  A, B, V = list(map(int, sys.stdin.readline().split()))

  day = (V-A)/(A-B)

  print(math.ceil(day) + 1)  





if __name__=="__main__":
  main()