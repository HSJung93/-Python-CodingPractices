


# def divide(string):
#   start, end = string.split(" ")
#   start_time = decode(start)
#   end_time = decode(end)
  
def decode(string):
  H, M, S = string.split(":")
  return int(H)*3600 + int(M)*60 + int(S)

def calc(input_string, start_list, end_list):
  pivot = decode(input_string)
  
  cnt = 0
  
  for start_time, end_time in zip(start_list, end_list):
    if start_time < pivot < end_time:
      cnt += 1
      
  return cnt

import sys

start_list =[]
end_list = []

for _ in range(3):
  start, end = sys.stdin.readline().split(" ")
  start_list.append(decod(start))
  end_list.append(decode(end))
  
  
calc("11:05:20", start_list, end_list)
  

      