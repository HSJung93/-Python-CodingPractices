def calc(arr):
  ret = [] * len(arr)
  temp = []
  for i, num in enumerate(arr):
    temp.append((num, i))

  temp.sort(key= x:x[0]), reversed=True)

  # [ (100, 0), (100,5), (96, 1) …
  prev = -1
  for index, num_set in enumerate(temp):
    num, i = num_set
    if perv == num:
      ret[i] = index+1

  return ret
